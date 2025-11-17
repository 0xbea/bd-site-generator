import unittest

from leafnode import LeafNode
from parentnode import ParentNode


def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


def test_to_html_with_children_with_props(self):
    child_node = LeafNode("span", "child", props=[("id", "child-class")])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(), '<div><span id="child-id">child</span></div>'
    )


def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )


def test_to_html_with_props(self):
    child_node = LeafNode("span", "child", props=[("class", "child-class")])
    parent_node = ParentNode("div", [child_node], props=[("id", "parent-id")])
    self.assertEqual(
        parent_node.to_html(),
        '<div id="parent-id"><span class="child-class">child</span></div>',
    )


def test_to_html_no_tag(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode(None, [child_node])
    with self.assertRaises(ValueError):
        parent_node.to_html()


def test_to_html_no_children(self):
    parent_node = ParentNode("div", None)
    with self.assertRaises(ValueError):
        parent_node.to_html()
