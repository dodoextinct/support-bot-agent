import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.angelone.in"

# List of main category pages (these contain multiple FAQs)
support_categories = [
    "https://www.angelone.in/support/add-and-withdraw-funds",
    "https://www.angelone.in/support/angel-one-recommendations",
    "https://www.angelone.in/support/charges-and-cashbacks",
    "https://www.angelone.in/support/charts",
    "https://www.angelone.in/support/complaince",
    "https://www.angelone.in/support/fixed-deposits",
    "https://www.angelone.in/support/ipo-ofs",
    "https://www.angelone.in/support/loans",
    "https://www.angelone.in/support/margin-pledging-and-margin-trading-facility",
    "https://www.angelone.in/support/mutual-funds",
    "https://www.angelone.in/support/portfolio-and-corporate-actions",
    "https://www.angelone.in/support/reports-and-statements",
    "https://www.angelone.in/support/your-account",
    "https://www.angelone.in/support/your-orders",
    "https://www.angelone.in/support/add-and-withdraw-funds/add-funds",
    "https://www.angelone.in/support/add-and-withdraw-funds/quarterly-settlement-sebi-payout",
    "https://www.angelone.in/support/add-and-withdraw-funds/withdraw-funds",
    "https://www.angelone.in/support/add-and-withdraw-funds/withdrawable-balance",
    "https://www.angelone.in/support/angel-one-recommendations/charges-and-frequency",
    "https://www.angelone.in/support/charges-and-cashbacks/dp-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/brokerage-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/stock-pledging-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/brokerage-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/stock-pledging-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/sebi-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/stt-securities-transaction-tax",
    "https://www.angelone.in/support/charges-and-cashbacks/stamp-duty",
    "https://www.angelone.in/support/charges-and-cashbacks/transaction-turnover-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/account-maintenance-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/auto-square-off-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/brokerage-cashback",
    "https://www.angelone.in/support/charges-and-cashbacks/brokerage-plan",
    "https://www.angelone.in/support/charges-and-cashbacks/call-and-trade-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/dp-depository-participant-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/gst-goods-services-tax",
    "https://www.angelone.in/support/charges-and-cashbacks/off-mkt-transaction-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/penal-delayed-payment-charges",
    "https://www.angelone.in/support/charges-and-cashbacks/pledging-charges",
    "https://www.angelone.in/support/complaince/risk-management-asm-gsm",
    "https://www.angelone.in/support/complaince/trading-surveillance",
    "https://www.angelone.in/support/charts/chart-not-loading",
    "https://www.angelone.in/support/charts/drawing-tools",
    "https://www.angelone.in/support/charts/indicators",
    "https://www.angelone.in/support/charts/multi-charts",
    "https://www.angelone.in/support/charts/trade-from-charts",
    "https://www.angelone.in/support/charts/others",
    "https://www.angelone.in/support/fixed-deposits/account-verification",
    "https://www.angelone.in/support/fixed-deposits/consent-security",
    "https://www.angelone.in/support/fixed-deposits/eligibility",
    "https://www.angelone.in/support/fixed-deposits/fixed-deposit-options",
    "https://www.angelone.in/support/fixed-deposits/payments-and-withdrawal",
    "https://www.angelone.in/support/fixed-deposits/post-purchase",
    "https://www.angelone.in/support/ipo-ofs/ipo",
    "https://www.angelone.in/support/ipo-ofs/ofs",
    "https://www.angelone.in/support/ipo-ofs/sovereign-gold-bonds-sgb",
    "https://www.angelone.in/support/ipo-ofs/stock-sip",
    "https://www.angelone.in/support/loans/active-loans",
    "https://www.angelone.in/support/loans/loans-enquiry",
    "https://www.angelone.in/support/loans/rejected-loans",
    "https://www.angelone.in/support/margin-pledging-and-margin-trading-facility/available-margin-to-trade",
    "https://www.angelone.in/support/margin-pledging-and-margin-trading-facility/margin-pledge-unpledge",
    "https://www.angelone.in/support/margin-pledging-and-margin-trading-facility/margin-trading-facility",
    "https://www.angelone.in/support/mutual-funds/orders",
    "https://www.angelone.in/support/mutual-funds/sips",
    "https://www.angelone.in/support/mutual-funds/investments",
    "https://www.angelone.in/support/portfolio-and-corporate-actions/bonus-issue",
    "https://www.angelone.in/support/portfolio-and-corporate-actions/buyback",
    "https://www.angelone.in/support/portfolio-and-corporate-actions/dividend",
    "https://www.angelone.in/support/portfolio-and-corporate-actions/holdings-portfolio",
    "https://www.angelone.in/support/portfolio-and-corporate-actions/rights-issue",
    "https://www.angelone.in/support/portfolio-and-corporate-actions/stock-split",
    "https://www.angelone.in/support/portfolio-and-corporate-actions/tpin",
    "https://www.angelone.in/support/reports-and-statements/client-master-list",
    "https://www.angelone.in/support/reports-and-statements/contract-note",
    "https://www.angelone.in/support/reports-and-statements/holding-statement",
    "https://www.angelone.in/support/reports-and-statements/ledger",
    "https://www.angelone.in/support/reports-and-statements/profit-loss",
    "https://www.angelone.in/support/reports-and-statements/trade-history-sauda-summary",
    "https://www.angelone.in/support/your-account/family-declaration",
    "https://www.angelone.in/support/your-account/online-account-opening",
    "https://www.angelone.in/support/your-account/account-settings-2",
    "https://www.angelone.in/support/your-account/subscription-plans",
    "https://www.angelone.in/support/your-account/other-services",
    "https://www.angelone.in/support/your-account/kyc-status",
    "https://www.angelone.in/support/your-account/dormant-account",
    "https://www.angelone.in/support/your-account/account-closure",
    "https://www.angelone.in/support/your-account/mpin-biometric",
    "https://www.angelone.in/support/your-account/mtf-activation-deactivation",
    "https://www.angelone.in/support/your-account/profile-details",
    "https://www.angelone.in/support/your-account/segment-activation",
    "https://www.angelone.in/support/your-orders/watchlist",
    "https://www.angelone.in/support/your-orders/basket-order",
    "https://www.angelone.in/support/your-orders/order-status",
    "https://www.angelone.in/support/your-orders/placing-an-order",
    "https://www.angelone.in/support/your-orders/robo-order",
    "https://www.angelone.in/support/your-orders/square-off",
    "https://www.angelone.in/support/your-orders/stop-loss-order",
    "https://www.angelone.in/support/your-orders/types-of-orders",
    "https://www.angelone.in/support/your-orders/limit-order",
    "https://www.angelone.in/support/your-orders/margin-calculator",
    "https://www.angelone.in/support/your-orders/options",
    "https://www.angelone.in/support/your-orders/order-rejection",
]

# Create output folder
os.makedirs("knowledge", exist_ok=True)

# Start scraping each category page
for url in support_categories:
    try:
        print(f"Scraping: {url}")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        page_slug = url.split("/")[-1]
        filename = os.path.join("knowledge", page_slug + ".md")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {page_slug.replace('-', ' ').title()}\n\n")

            # Grab all FAQ sections
            tabs = soup.find_all("div", class_="tab")
            if not tabs:
                f.write("_No FAQs found on this page._\n")

            for tab in tabs:
                question = tab.find("label", class_="tab-label")
                answer = tab.find("div", class_="tab-content")

                if question and answer:
                    q_text = question.get_text(strip=True).replace("Vector", "")
                    a_text = answer.get_text(separator="\n", strip=True)
                    f.write(f"## {q_text}\n\n{a_text}\n\n---\n\n")
                else:
                    print("⚠️ Skipped one empty tab.")

        print(f"✅ Saved: {filename}")

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
