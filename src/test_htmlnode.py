import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_noprops(self):
        node = HTMLNode("p", "this is a paragraph").props_to_html()
        result = ""
        self.assertEqual(node, result)

    def test_hasprops(self):
        node = HTMLNode(
            "p", "this is a paragraph", props=[("class", "text"), ("id", "para1")]
        ).props_to_html()
        result = ' class="text" id="para1"'
        self.assertEqual(node, result)

    def test_links_eq(self):
        node = HTMLNode(
            "a", "click here", props=[("href", "http://example.com")]
        ).props_to_html()
        result = ' href="http://example.com"'
        self.assertEqual(node, result)


if __name__ == "__main__":
    unittest.main()
