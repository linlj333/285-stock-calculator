from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def send():
    if request.method == 'POST':
        symbol = request.form['symbol']
        allotment = request.form['allotment']
        finalSharePrice = request.form['finalSharePrice']
        sellCommission = request.form['sellCommission']
        iniSharePrice = request.form['iniSharePrice']
        buyCommission = request.form['buyCommission']
        cgtr = request.form['cgtr']
        proceeds = float(allotment) * float(finalSharePrice)
        proceedsDisplay = "$%.2f" % proceeds
        totalPurchasePrice = float(allotment) * float(iniSharePrice)
        totalPurchasePriceDis = "$%.2f" % totalPurchasePrice
        taxOncg = (float(proceeds) - float(totalPurchasePrice) - float(sellCommission) - float(buyCommission)) * float(cgtr) * 0.01
        cost = float(totalPurchasePrice) + float(sellCommission) + float(buyCommission) + float(taxOncg)
        netProfit = float(proceeds - cost)
        returnOnInvestment = float(netProfit) / float(cost) * 100
        returnOnInvestmentDisplay = "$%.2f" % returnOnInvestment
        breakEven = (float(allotment) * float(iniSharePrice) + float(sellCommission) + float(buyCommission))/float(allotment)
        return render_template('display.html', symbol = symbol, allotment = allotment, finalSharePrice = finalSharePrice,
                               sellCommission = sellCommission, iniSharePrice = iniSharePrice,
                               buyCommission = buyCommission, totalPurchasePriceDis = totalPurchasePriceDis,  cgtr = cgtr,
                               proceedsDisplay = proceedsDisplay,cost =cost, taxOncg=taxOncg, netProfit=netProfit,
                               returnOnInvestmentDisplay = returnOnInvestmentDisplay, breakEven =breakEven)



    return render_template('index.html')


if __name__ == '__main__':
    app.run()

# "%0.2f" %
#