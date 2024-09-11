"""
This is a boilerplate pipeline 'expense_analysis'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, node

from .nodes import (
    analyze_expenses_per_party,
    find_largest_expense_source,
    find_top_overall_spender,
    find_top_spender_per_party,
    find_top_spending_party,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=analyze_expenses_per_party,
                inputs=["congress_expenses", "parameters"],
                outputs="expenses_per_party",
                name="analyze_expenses_per_party_node",
            ),
            node(
                func=find_largest_expense_source,
                inputs=["congress_expenses", "parameters"],
                outputs="largest_expense_source",
                name="find_largest_expense_source_node",
            ),
            node(
                func=find_top_spender_per_party,
                inputs=["expenses_per_party", "parameters"],
                outputs="top_spender_per_party",
                name="find_top_spender_per_party_node",
            ),
            node(
                func=find_top_overall_spender,
                inputs=["top_spender_per_party", "parameters"],
                outputs="top_overall_spender",
                name="find_top_overall_spender_node",
            ),
            node(
                func=find_top_spending_party,
                inputs=["expenses_per_party", "parameters"],
                outputs="top_spending_party",
                name="find_top_spending_party_node",
            ),
        ]
    )
