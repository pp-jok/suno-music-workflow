from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
REQUIRED = {
    "01-locked-chorus.md",
    "02-feels-ordinary.md",
    "03-pop-energy.md",
    "04-stochastic-ab-test.md",
    "05-style-compression.md",
}
FIELDS = ("## 起点", "## 固定", "## 只改", "## 期待听感", "## 证据与置信度", "## 下一步")
TAGS = ("[Objective evidence]", "[User feedback]", "[Editorial judgement]", "[Inference]")


class ReadableExamplesTests(unittest.TestCase):
    def test_public_entry_points_describe_and_link_the_validation_cases(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        for phrase in (
            "Hooks",
            "production plans",
            "controlled iteration",
            "evidence-bounded",
            "examples/",
        ):
            self.assertIn(phrase, skill)
        self.assertNotIn("Suno Studio is required", skill)
        self.assertIn("examples/", readme)

        self.assertIn(
            "description: Create Chinese songs with Hooks, production plans, Suno Style prompts, "
            "controlled iteration, and evidence-bounded audio review. Use when a user asks to turn "
            "a song idea into a Hook, lyrics, a production plan, a Suno prompt, feedback-led "
            "revisions, audio diagnosis, or LRC timestamps.",
            skill,
        )
        self.assertIn(
            "For concise creator-readable examples of controlled revisions, read "
            "[the validation cases](examples/).",
            skill,
        )
        self.assertIn("## 从案例开始", readme)
        for name in REQUIRED:
            self.assertIn(f"(examples/{name})", readme)
        for term in ("虚构", "保证", "官方"):
            self.assertIn(term, readme)

    def test_five_examples_use_the_common_creator_card(self):
        self.assertEqual({path.name for path in EXAMPLES.glob("*.md")}, REQUIRED)
        for name in REQUIRED:
            text = (EXAMPLES / name).read_text(encoding="utf-8")
            for field in FIELDS:
                self.assertIn(field, text)
            self.assertTrue(any(tag in text for tag in TAGS))

    def test_generation_loop_calibrates_matched_experiments_with_evidence_tags(self):
        text = (ROOT / "references" / "generation-loop.md").read_text(encoding="utf-8")
        required_phrases = (
            "Baseline A",
            "treatment B",
            "same approved choices",
            "same candidate count",
            "Low",
            "Medium",
            "High",
            "[Objective evidence]",
            "[User feedback]",
            "[Editorial judgement]",
            "[Inference]",
        )
        for phrase in required_phrases:
            self.assertIn(phrase, text)

    def test_generation_loop_requires_consistent_agreement_and_distinct_evidence_roles(self):
        text = (ROOT / "references" / "generation-loop.md").read_text(encoding="utf-8")

        medium = next(line for line in text.splitlines() if line.startswith("- **Medium:"))
        high = next(line for line in text.splitlines() if line.startswith("- **High:"))
        self.assertIn("consistent direction", medium)
        self.assertIn("user feedback agree", high)
        self.assertIn("creator's report", text)
        self.assertIn("producer or reviewer's interpretation", text)

    def test_ordinary_example_keeps_the_rhythm_hypothesis_open(self):
        text = (EXAMPLES / "02-feels-ordinary.md").read_text(encoding="utf-8")

        self.assertIn("does not support the rhythm hypothesis yet", text)
        self.assertIn("does not rule it out", text)

    def test_ab_plan_is_an_inference_until_audio_exists(self):
        text = (EXAMPLES / "04-stochastic-ab-test.md").read_text(encoding="utf-8")

        self.assertIn("no generation or audio observation exists yet", text)
        self.assertIn("[Inference]", text)
        self.assertNotIn("[Objective evidence]", text)

    def test_style_compression_waits_for_required_input_and_check(self):
        text = (EXAMPLES / "05-style-compression.md").read_text(encoding="utf-8")

        for phrase in ("置信度：低", "[Inference]", "source Style", "avoid constraint", "1,000"):
            self.assertIn(phrase, text)
        self.assertNotIn("置信度：中", text)


if __name__ == "__main__":
    unittest.main()
