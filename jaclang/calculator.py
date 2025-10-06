"""Simple, safe-ish calculator functions for demo purposes.

This module exposes `evaluate(expr: str) -> float|int` that computes a basic
arithmetic expression using Python AST to avoid eval on untrusted input.
"""
from __future__ import annotations

import ast
import operator as op
from typing import Union

# supported operators
_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.Mod: op.mod,
}

Number = Union[int, float]


def _eval_node(node: ast.AST) -> Number:
    if isinstance(node, ast.Num):  # type: ignore[attr-defined]
        return node.n  # type: ignore[attr-defined]
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in _OPERATORS:
            return _OPERATORS[op_type](left, right)
        raise ValueError(f"Unsupported binary operator: {op_type}")
    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)
        if op_type in _OPERATORS:
            return _OPERATORS[op_type](operand)
        raise ValueError(f"Unsupported unary operator: {op_type}")
    raise ValueError(f"Unsupported expression node: {node!r}")


def evaluate(expr: str) -> Number:
    """Evaluate a simple arithmetic expression (numbers and + - * / % ** and unary -).

    Examples:
        evaluate("2 + 3 * 4") -> 14
        evaluate("-5 + 2") -> -3
    """
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"Invalid expression: {e}") from e

    return _eval_node(tree.body)
