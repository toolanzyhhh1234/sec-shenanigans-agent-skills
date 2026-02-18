#!/usr/bin/env python3
"""
Financial Sheets Fetcher
Fetches yearly and quarterly financial statements (Income Statement, Balance Sheet, Cash Flow)
and exports them to a single markdown file for easy sharing.
"""

import json
import argparse
from datetime import datetime
import pandas as pd
import yfinance as yf
import os


def format_dataframe_to_markdown(df, max_rows=50):
    """Convert DataFrame to markdown table format, truncating if needed."""
    if df.empty:
        return "No data available"

    # Limit rows for readability
    if len(df) > max_rows:
        df_display = df.head(max_rows)
        note = f"\n*Note: Showing first {max_rows} rows out of {len(df)} total rows*\n"
    else:
        df_display = df
        note = ""

    markdown = df_display.to_markdown(index=True)
    return markdown + note if markdown else "No data available"


def fetch_financial_statements(ticker):
    """Fetch all financial statements for a ticker."""
    print(f"Fetching financial data for {ticker}...")

    try:
        company = yf.Ticker(ticker)

        # Verify ticker exists
        if company.isin is None:
            return None, f"Error: Company ticker {ticker} not found."

        statements = {
            "yearly": {},
            "quarterly": {},
            "historical_prices": {},
            "stock_info": None,
            "news": None,
            "holders": {},
            "recommendations": None,
        }

        # Fetch yearly statements
        try:
            statements["yearly"]["income_stmt"] = company.income_stmt
            print(f"  ✓ Yearly Income Statement")
        except Exception as e:
            statements["yearly"]["income_stmt"] = None
            print(f"  ✗ Yearly Income Statement: {e}")

        try:
            statements["yearly"]["balance_sheet"] = company.balance_sheet
            print(f"  ✓ Yearly Balance Sheet")
        except Exception as e:
            statements["yearly"]["balance_sheet"] = None
            print(f"  ✗ Yearly Balance Sheet: {e}")

        try:
            statements["yearly"]["cashflow"] = company.cashflow
            print(f"  ✓ Yearly Cash Flow")
        except Exception as e:
            statements["yearly"]["cashflow"] = None
            print(f"  ✗ Yearly Cash Flow: {e}")

        # Fetch quarterly statements
        try:
            statements["quarterly"]["income_stmt"] = company.quarterly_income_stmt
            print(f"  ✓ Quarterly Income Statement")
        except Exception as e:
            statements["quarterly"]["income_stmt"] = None
            print(f"  ✗ Quarterly Income Statement: {e}")

        try:
            statements["quarterly"]["balance_sheet"] = company.quarterly_balance_sheet
            print(f"  ✓ Quarterly Balance Sheet")
        except Exception as e:
            statements["quarterly"]["balance_sheet"] = None
            print(f"  ✗ Quarterly Balance Sheet: {e}")

        try:
            statements["quarterly"]["cashflow"] = company.quarterly_cashflow
            print(f"  ✓ Quarterly Cash Flow")
        except Exception as e:
            statements["quarterly"]["cashflow"] = None
            print(f"  ✗ Quarterly Cash Flow: {e}")

        # Fetch historical prices - 1 year with 1 month interval
        try:
            hist_1y_1mo = company.history(period="1y", interval="1mo")
            hist_1y_1mo = hist_1y_1mo.reset_index()
            statements["historical_prices"]["1y_1mo"] = hist_1y_1mo
            print(f"  ✓ Historical Prices (1 year, 1 month interval)")
        except Exception as e:
            statements["historical_prices"]["1y_1mo"] = None
            print(f"  ✗ Historical Prices (1y, 1mo): {e}")

        # Fetch historical prices - 1 week with 1 day interval
        try:
            hist_1wk_1d = company.history(period="1wk", interval="1d")
            hist_1wk_1d = hist_1wk_1d.reset_index()
            statements["historical_prices"]["1wk_1d"] = hist_1wk_1d
            print(f"  ✓ Historical Prices (1 week, 1 day interval)")
        except Exception as e:
            statements["historical_prices"]["1wk_1d"] = None
            print(f"  ✗ Historical Prices (1wk, 1d): {e}")

        # Fetch stock info
        try:
            statements["stock_info"] = company.info
            print(f"  ✓ Stock Info")
        except Exception as e:
            statements["stock_info"] = None
            print(f"  ✗ Stock Info: {e}")

        # Fetch news
        try:
            statements["news"] = company.news
            print(f"  ✓ News")
        except Exception as e:
            statements["news"] = None
            print(f"  ✗ News: {e}")

        # Fetch holder information
        try:
            statements["holders"]["major_holders"] = company.major_holders
            print(f"  ✓ Major Holders")
        except Exception as e:
            statements["holders"]["major_holders"] = None
            print(f"  ✗ Major Holders: {e}")

        try:
            statements["holders"]["institutional_holders"] = (
                company.institutional_holders
            )
            print(f"  ✓ Institutional Holders")
        except Exception as e:
            statements["holders"]["institutional_holders"] = None
            print(f"  ✗ Institutional Holders: {e}")

        try:
            statements["holders"]["mutualfund_holders"] = company.mutualfund_holders
            print(f"  ✓ Mutual Fund Holders")
        except Exception as e:
            statements["holders"]["mutualfund_holders"] = None
            print(f"  ✗ Mutual Fund Holders: {e}")

        try:
            statements["holders"]["insider_transactions"] = company.insider_transactions
            print(f"  ✓ Insider Transactions")
        except Exception as e:
            statements["holders"]["insider_transactions"] = None
            print(f"  ✗ Insider Transactions: {e}")

        # Fetch recommendations
        try:
            statements["recommendations"] = company.recommendations
            print(f"  ✓ Recommendations")
        except Exception as e:
            statements["recommendations"] = None
            print(f"  ✗ Recommendations: {e}")

        return statements, None

    except Exception as e:
        return None, f"Error fetching data: {e}"


def generate_markdown_report(ticker, statements):
    """Generate a comprehensive markdown report from financial statements."""

    report = []
    report.append(f"# Financial Statements Report: {ticker.upper()}")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Table of Contents
    report.append("## Table of Contents\n")
    report.append("1. [Stock Information](#stock-information)")
    report.append("2. [Historical Prices](#historical-prices)")
    report.append("3. [News](#news)")
    report.append("4. [Holder Information](#holder-information)")
    report.append("5. [Recommendations](#recommendations)")
    report.append("6. [Yearly Income Statement](#yearly-income-statement)")
    report.append("7. [Yearly Balance Sheet](#yearly-balance-sheet)")
    report.append("8. [Yearly Cash Flow](#yearly-cash-flow)")
    report.append("9. [Quarterly Income Statement](#quarterly-income-statement)")
    report.append("10. [Quarterly Balance Sheet](#quarterly-balance-sheet)")
    report.append("11. [Quarterly Cash Flow](#quarterly-cash-flow)\n")

    # Stock Information
    report.append("---\n")
    report.append("## Stock Information\n")
    if statements["stock_info"] is not None:
        info = statements["stock_info"]
        # Format key stock info as a readable table
        key_metrics = [
            ("Symbol", info.get("symbol", "N/A")),
            ("Company Name", info.get("longName", "N/A")),
            ("Sector", info.get("sector", "N/A")),
            ("Industry", info.get("industry", "N/A")),
            ("Current Price", info.get("currentPrice", "N/A")),
            ("Market Cap", info.get("marketCap", "N/A")),
            ("P/E Ratio", info.get("trailingPE", "N/A")),
            ("EPS", info.get("trailingEps", "N/A")),
            ("52 Week High", info.get("fiftyTwoWeekHigh", "N/A")),
            ("52 Week Low", info.get("fiftyTwoWeekLow", "N/A")),
            ("Dividend Yield", info.get("dividendYield", "N/A")),
            ("Website", info.get("website", "N/A")),
        ]
        report.append("| Metric | Value |")
        report.append("|--------|-------|")
        for metric, value in key_metrics:
            report.append(f"| {metric} | {value} |")
        report.append("\n")
    else:
        report.append("*No stock information available*\n")

    # Historical Prices
    report.append("---\n")
    report.append("## Historical Prices\n")

    # 1 year, 1 month interval
    report.append("### Historical Prices (1 Year, 1 Month Interval)\n")
    if statements["historical_prices"].get("1y_1mo") is not None:
        report.append(
            format_dataframe_to_markdown(statements["historical_prices"]["1y_1mo"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    # 1 week, 1 day interval
    report.append("### Historical Prices (1 Week, 1 Day Interval)\n")
    if statements["historical_prices"].get("1wk_1d") is not None:
        report.append(
            format_dataframe_to_markdown(statements["historical_prices"]["1wk_1d"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    # News
    report.append("---\n")
    report.append("## News\n")
    if statements["news"] is not None and len(statements["news"]) > 0:
        for idx, article in enumerate(
            statements["news"][:10], 1
        ):  # Limit to 10 most recent
            # Handle nested content structure
            content = article.get("content", article)
            title = content.get("title", "No Title")
            provider = content.get("provider", {})
            publisher_name = (
                provider.get("displayName", "N/A")
                if isinstance(provider, dict)
                else "N/A"
            )

            # Get canonical URL
            canonical_url = content.get("canonicalUrl", {})
            link = (
                canonical_url.get("url", "#")
                if isinstance(canonical_url, dict)
                else "#"
            )

            # Get publish date
            pub_date = content.get("pubDate", None)
            if pub_date:
                try:
                    from dateutil import parser

                    date_str = parser.parse(pub_date).strftime("%Y-%m-%d %H:%M:%S")
                except:
                    date_str = pub_date
            else:
                date_str = "N/A"

            report.append(f"### {idx}. {title}\n")
            report.append(f"**Publisher:** {publisher_name}  ")
            report.append(f"**Published:** {date_str}\n")
            report.append(f"**Link:** [{link}]({link})\n")
            report.append("\n")
    else:
        report.append("*No news available*\n")

    # Holder Information
    report.append("---\n")
    report.append("## Holder Information\n")

    report.append("### Major Holders\n")
    if statements["holders"].get("major_holders") is not None:
        report.append(
            format_dataframe_to_markdown(statements["holders"]["major_holders"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    report.append("### Institutional Holders\n")
    if statements["holders"].get("institutional_holders") is not None:
        report.append(
            format_dataframe_to_markdown(statements["holders"]["institutional_holders"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    report.append("### Mutual Fund Holders\n")
    if statements["holders"].get("mutualfund_holders") is not None:
        report.append(
            format_dataframe_to_markdown(statements["holders"]["mutualfund_holders"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    report.append("### Insider Transactions\n")
    if statements["holders"].get("insider_transactions") is not None:
        report.append(
            format_dataframe_to_markdown(statements["holders"]["insider_transactions"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    # Recommendations
    report.append("---\n")
    report.append("## Recommendations\n")
    if statements["recommendations"] is not None:
        report.append(format_dataframe_to_markdown(statements["recommendations"]))
    else:
        report.append("*No recommendations available*")
    report.append("\n")

    # Yearly Statements
    report.append("---\n")
    report.append("## Yearly Financial Statements\n")

    # Yearly Income Statement
    report.append("### Yearly Income Statement\n")
    if statements["yearly"]["income_stmt"] is not None:
        report.append(format_dataframe_to_markdown(statements["yearly"]["income_stmt"]))
    else:
        report.append("*No data available*")
    report.append("\n")

    # Yearly Balance Sheet
    report.append("### Yearly Balance Sheet\n")
    if statements["yearly"]["balance_sheet"] is not None:
        report.append(
            format_dataframe_to_markdown(statements["yearly"]["balance_sheet"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    # Yearly Cash Flow
    report.append("### Yearly Cash Flow\n")
    if statements["yearly"]["cashflow"] is not None:
        report.append(format_dataframe_to_markdown(statements["yearly"]["cashflow"]))
    else:
        report.append("*No data available*")
    report.append("\n")

    # Quarterly Statements
    report.append("---\n")
    report.append("## Quarterly Financial Statements\n")

    # Quarterly Income Statement
    report.append("### Quarterly Income Statement\n")
    if statements["quarterly"]["income_stmt"] is not None:
        report.append(
            format_dataframe_to_markdown(statements["quarterly"]["income_stmt"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    # Quarterly Balance Sheet
    report.append("### Quarterly Balance Sheet\n")
    if statements["quarterly"]["balance_sheet"] is not None:
        report.append(
            format_dataframe_to_markdown(statements["quarterly"]["balance_sheet"])
        )
    else:
        report.append("*No data available*")
    report.append("\n")

    # Quarterly Cash Flow
    report.append("### Quarterly Cash Flow\n")
    if statements["quarterly"]["cashflow"] is not None:
        report.append(format_dataframe_to_markdown(statements["quarterly"]["cashflow"]))
    else:
        report.append("*No data available*")
    report.append("\n")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch financial statements for a ticker and export to markdown"
    )
    parser.add_argument("ticker", help="Stock ticker symbol (e.g., AAPL, MSFT)")
    parser.add_argument(
        "-o",
        "--output",
        help="Output markdown file (default: {ticker}_financial_statements.md)",
        default=None,
    )

    args = parser.parse_args()
    raw_ticker = args.ticker
    tickers = [t.strip().upper() for t in raw_ticker.split(",") if t.strip()]

    if not tickers:
        print(" No valid tickers provided.")
        return 1

    # Base directory for output is the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    exit_code = 0

    for ticker in tickers:
        print(f"\n=== Processing {ticker} ===")

        # Create ticker-specific directory
        ticker_dir = os.path.join(script_dir, ticker)
        os.makedirs(ticker_dir, exist_ok=True)

        if args.output and len(tickers) == 1:
            if os.path.isabs(args.output):
                output_file = args.output
            else:
                output_file = os.path.join(ticker_dir, args.output)
        elif args.output and len(tickers) > 1:
            if os.path.isabs(args.output):
                out_dir, out_name = os.path.split(args.output)
                base_name, ext = os.path.splitext(out_name)
                # If specific output directory is provided, we respect that,
                # but for simplicity if it's just a name we use ticker_dir.
                current_out_dir = out_dir if out_dir else ticker_dir
            else:
                current_out_dir = ticker_dir
                base_name, ext = os.path.splitext(args.output)

            if ext:
                output_file = os.path.join(
                    current_out_dir, f"{base_name}_{ticker}{ext}"
                )
            else:
                output_file = os.path.join(current_out_dir, f"{base_name}_{ticker}.md")
        else:
            output_file = os.path.join(ticker_dir, f"{ticker}_financial_statements.md")

        # Fetch statements
        statements, error = fetch_financial_statements(ticker)
        if error:
            print(f"\n {error}")
            exit_code = 1
            continue

        # Generate report
        print(f"\nGenerating markdown report...")
        markdown_report = generate_markdown_report(ticker, statements)

        # Write to file
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(markdown_report)
            print(f"✓ Report saved to: {output_file}")
            print(f"✓ File size: {len(markdown_report):,} bytes")
        except Exception as e:
            print(f"❌ Error writing file for {ticker}: {e}")
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    exit(main())
