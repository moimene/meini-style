"""Checks installation paths in INSTALL.md (and translations, when present)."""

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class ZedInstallPathTest(unittest.TestCase):
    def test_zed_install_paths(self):
        translations = sorted((ROOT / ".github/install").glob("INSTALL.*.md"))
        for path in [ROOT / "INSTALL.md", *translations]:
            with self.subTest(file=path.name):
                text = path.read_text(encoding="utf8")
                marker = "<summary><strong>Zed</strong></summary>"
                self.assertIn(marker, text)
                section = text.split(marker, 1)[1]
                self.assertIn("</details>", section)
                section = section.split("</details>", 1)[0]

                self.assertNotIn("~/.config/zed/skills", section)
                self.assertIn(
                    "mkdir -p ~/.agents/skills\n"
                    "cp -R meini-style/skills/meini-style ~/.agents/skills/",
                    section,
                )
                self.assertIn("~/.agents/skills/meini-style", section)


class GrokInstallPathTest(unittest.TestCase):
    def test_grok_install_commands(self):
        text = (ROOT / "INSTALL.md").read_text(encoding="utf8")
        marker = "<summary><strong>Grok (<code>grok</code>)</strong></summary>"
        self.assertIn(marker, text)
        section = text.split(marker, 1)[1]
        self.assertIn("</details>", section)
        section = section.split("</details>", 1)[0]

        self.assertIn("grok plugin install moimene/meini-style --trust", section)
        self.assertIn("grok plugin enable meini-style", section)
        self.assertIn("grok plugin update meini-style", section)
        self.assertIn("grok plugin uninstall meini-style --confirm", section)
        self.assertIn("/meini-style", section)
        self.assertIn("~/.grok/AGENTS.md", section)
        self.assertIn("~/.grok/rules/meini-style.md", section)
        self.assertNotIn("~/.claude/.meini-style-always", section)


if __name__ == "__main__":
    unittest.main()
