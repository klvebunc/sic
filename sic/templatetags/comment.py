import collections
from django import template
from django.conf import settings
from django.utils.http import urlencode
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.template.defaulttags import URLNode, url
from django.template.exceptions import TemplateSyntaxError
from django.template.base import Token, Node, kwarg_re
from django.template import Context, Template
from django.template.loader import render_to_string
import collections

register = template.Library()


class Comment:
    def __init__(self, obj):
        self.parent = obj.parent_id
        self.children = []
        self.obj = obj

    def __str__(self):
        return f"p {self.parent} c {self.children} obj {self.obj}"

    def __repr__(self):
        return str(self)


@register.simple_tag(takes_context=True)
def render_comments(
    context,
    request,
    comments,
    reply_form,
    level=1,
    edit_comment_pk=None,
    edit_comment_form=None,
):

    comments = {c.id: Comment(c) for c in comments}
    rendered = {c: None for c in comments}
    for c in comments:
        if comments[c].parent is not None:
            comments[comments[c].parent].children.append(c)

    order_q = collections.deque()
    q = collections.deque((level, c) for c in comments if comments[c].parent is None)
    while len(q) != 0:
        (level, root) = q.pop()
        order_q.append((level, root))
        if len(comments[root].children) > 0:
            for c in comments[root].children:
                q.append((level + 1, c))

    while len(order_q) != 0:
        (lvl, leaf) = order_q.pop()
        children = comments[leaf].children
        replies = [rendered[c] for c in children]
        rendered[leaf] = render_to_string(
            "posts/comment.html",
            context={
                "comment": comments[leaf].obj,
                "replies": replies,
                "reply_form": reply_form,
                "level": lvl,
                "edit_comment_pk": edit_comment_pk,
                "edit_comment_form": edit_comment_form,
            },
            request=request,
        )

    ret = "".join(rendered[c] for c in comments if comments[c].parent is None)
    return mark_safe(ret)
