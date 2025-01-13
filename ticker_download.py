import pandas as pd
import json

# Specify the path to your CSV file
csv_file = "/Users/giacomomaggiore/Desktop/flat-ui__data-Sun Dec 15 2024.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

sp500_list = []


for index, row in df.iterrows():
    
    sp500_list.append({
        "name": row["Security"],
        "ticker": row["Symbol"]
    }
    )
   


    
etf=[["iShares Core S&P 500","CSSPX",0.07,False],["iShares Core MSCI World","SWDA",0.20,True],["iShares Core MSCI Emerging Markets IMI","EIMI",0.18,True],
     ["iShares Nasdaq 100","CSNDX",0.33,False],["iShares MSCI ACWI","IUSQ",0.20,True],["Vanguard FTSE All-World","VWCE",0.22,True],
     ["iShares Core DAX","EXS1",0.16,False],["Lyxor Core STOXX Europe 600 (DR)","MEUD",0.07,True],["iShares Core MSCI Europe","SMEA",0.12,True],
     ["Xtrackers MSCI USA","XD9U",0.07,False],["Xtrackers MSCI Emerging Markets","XMME",0.18,True],["iShares Core EURO STOXX 50","CSSX5E",0.10,True],
     ["iShares Edge MSCI World Value Factor","IWVL",0.30,True],["iShares Core MSCI Japan IMI","SJPA",0.15,False],["iShares Core MSCI EMU","CSEMU",0.12,True],
     ["iShares Edge MSCI World Minimum Volatility","MVOL",0.30,True],["iShares Edge MSCI Europe Value Factor","IEVL",0.25,True],
     ["iShares Core MSCI Pacific ex Japan","CSPXJ",0.20,True],["Xtrackers S&P 500 Equal Weight","XDEW",0.20,False],["iShares MSCI World Small Cap","IUSN",0.35,True],
     ["iShares Edge MSCI World Quality Factor","IWQU",0.30,True],["iShares MSCI EM Asia","CSEMAS",0.20,True],["UBS ETF (LU) MSCI UK","UKGBPB",0.20,False],
     ["SPDR S&P 400 US Mid Cap","SPY4",0.30,False],["iShares Edge S&P 500 Minimum Volatility","MVUS",0.20,False],
     ["UBS ETF (LU) MSCI Switzerland 20/35","SW2CHB",0.20,False],["SPDR Russell 2000 US Small Cap","R2US",0.30,False],["iShares MSCI Canada","CSCA",0.48,False],
     ["Xtrackers MSCI China","XCS6",0.65,False],["Amundi CAC 40","C40",0.25,False],["Xtrackers MSCI Europe Small Cap","XXSC",0.30,True],
     ["Vanguard FTSE North America","VNRA",0.10,True],["Amundi ETF MSCI Europe Value Factor","VCEU",0.23,True],["Amundi MSCI Europe Quality Factor","QCEU",0.23,True],
     ["iShares MSCI Australia","SAUS",0.50,False],["Amundi ETF MSCI World ex EMU","CM9",0.35,True],
     ["Franklin FTSE Korea","FLXK",0.09,False],["WisdomTree US Quality Dividend Growth","DGRA",0.33,False],["Lyxor MSCI Brazil","BRA",0.65,False],
     ["Lyxor MSCI Emerging Markets Ex China","EMXC",0.15,True],["Vanguard FTSE Emerging Markets","VFEA",0.22,True],["iShares Edge MSCI World Size Factor","IWSZ",0.30,False],
     ["Amundi Japan Topix","XAMY",0.20,False],["Vanguard FTSE Developed Europe ex UK","VERE",0.10,False],["Fidelity US Quality Income","FUSA",0.25,False],
     ["Franklin FTSE China","FLXC",0.19,False],["iShares MSCI UK Small Cap","SXRD",0.58,False],["Franklin FTSE India","FLXI",0.19,False],
     ["iShares Nikkei 225","CSNKY",0.48,False],["Amundi MSCI Nordic","CN1",0.25,False],["iShares Edge MSCI Europe Multifactor","IFSE",0.45,True],
     ["Amundi MSCI Europe Minimum Volatility Factor","MIVO",0.23,True],["iShares MSCI EMU Large Cap","EMUL",0.49,True],["Xtrackers MSCI North America High Dividend Yield","XDND",0.39,False],
     ["Amundi ETF MSCI Switzerland","18MN",0.25,False],["iShares MSCI EMU Mid Cap","IS3H",0.49,True],["iShares MSCI Korea","CSKR",0.65,False],
     ["SPDR MSCI Europe Small Cap","SMCX",0.30,True],["Xtrackers MSCI Mexico","XMEX",0.65,False],["Lyxor MSCI Eastern Europe ex Russia","EST",0.50,False],
     ["iShares Edge MSCI USA Size Factor","QDVC",0.20,False],["SPDR MSCI USA Value Weighted","ZPRU",0.20,False],["Xtrackers MSCI Taiwan","XMTW",0.65,False]]

etf_list = []

for etf in etf:
    etf_list.append({
        "name": etf[0],
        "ticker": etf[1]+".MI"
    })
    
    

asset_list = etf_list + sp500_list
print(asset_list)