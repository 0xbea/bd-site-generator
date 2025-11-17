import unittest

from leafnode import LeafNode


def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


def test_leaf_to_html_div_with_props(self):
    node = LeafNode(
        "div", "Content here", props=[("class", "container"), ("id", "main")]
    )
    self.assertEqual(
        node.to_html(), '<div class="container" id="main">Content here</div>'
    )


def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Just some text")
    self.assertEqual(node.to_html(), "Just some text")


def test_leaf_to_html_no_value(self):
    node = LeafNode("span", None)
    with self.assertRaises(ValueError):
        node.to_html()
