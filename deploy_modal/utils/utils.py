import yfinance as yf
def get_stock_info(tickers = ["PETR3.SA", "PETR4.SA"]):
    dados = yf.Tickers(" ".join(tickers))
    for codigo in tickers:
        info = dados.tickers[codigo].fast_info
        preco = info.get("lastPrice") or info.get("previousClose")
        abertura = info.get("open")
        maxima = info.get("dayHigh")
        minima = info.get("dayLow")
        variacao_pct = info.get("percentChange")

        if variacao_pct is not None and isinstance(variacao_pct, (int, float)):
            sinal = "📈" if variacao_pct >= 0 else "📉"
            print(
                f"{sinal} {codigo}: R$ {preco:.2f} | "
                f"Variação: {variacao_pct:+.2f}%"
            )
        else:
            print(f"✅ {codigo}: R$ {preco:.2f}")

        if abertura and maxima and minima:
            print(
                f"   Abertura: R$ {abertura:.2f} | "
                f"Máxima: R$ {maxima:.2f} | Mínima: R$ {minima:.2f}"
            )
            
if __name__ == "__main__":
    get_stock_info()