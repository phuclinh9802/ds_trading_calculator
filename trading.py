# parameters: current_balance, # of months, debit_spread_price

import xlsxwriter
from datetime import datetime, timedelta

def ds_calculator(date_string, current_balance, number_of_months, debit_spread_price):
# example: price = 75 ->
                # larger condition: if current_balance < 2000
                  # condition: if price*# of contracts < current_balance
                  # -> profit = (100-price)*# of contracts
                  # -> current_balance += profit
                  # -> move current_balance, profits, and contract(s) to 2-d list
                # larger condition: if current_balance > 2000 and current_balance < 5000
                  #  condition: if price* # of contracts < current_balance - 200
                # even larger condition: if current_price >= 5000 and current_price < 10000
                  # condition: if price * # of contracts < current_balance - 500
                # ultra condition: if current_price >= 10000 and current_price < 20000 (some serious saving money)
                  # condition: if price * # of contracts < current_balance - 2000
                # super condition: if current_price >= 20000 and current_price < 50000 (almost getting salary for 1 year)
                  # condition: if price * # of contracts < current_balance - 5000
                # super duper condition: if current_price >= 50000 and current_price < 100000 (getting rich)
                  # condition: if price * # of contracts < current_balance - 10000
                # tech-company-salary condition: if current_price >= 100000 and current_price < 200000 (start considering new life plan)
                  # condition: if price * # of contracts < current_balance - 20000
                # manager-like condition: if current_price >= 200000 and current_price < 500000 (like a manager)
                  # condition: if price * # of contracts < current_balance - 50000
                # becoming-millionaire condition: if current_price >= 500000 and current_price < 1000000 (might be happening)
                  # condition: if price * # of contracts < current_balance - 100000
                # millionaire condition: if current_price >= 1000000
                  # condition: if price * # of contracts < current_balance - 200000
    profit = 0.0
    contracts = 1
    table = []
    date = datetime(year=int(date_string[0:4]), month=int(date_string[4:6]), day=int(date_string[6:8]))
    date_list = ["date", date_string]
    profit_list = ["profits", 0]
    balance_list = ["balance", current_balance]
    contract_list = ["contracts", 0]
    m = 1


    s = date.strftime("%Y%m%d")
    while m < number_of_months:
        if current_balance < 2000:
            if debit_spread_price * contracts < current_balance:
                contracts += 1
            else:
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                contracts -= 1
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
                # specific_calculator(current_balance + profit, profit, debit_spread_price, contracts, profit_list, balance_list, contract_list

        elif current_balance >= 2000.0 and current_balance < 5000.0:
            if debit_spread_price * contracts < current_balance - 200:
                contracts += 1

            else:
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                contracts -= 1
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 5000 and current_balance < 10000:
            if debit_spread_price * contracts < current_balance - 500:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 10000 and current_balance < 20000:
            if debit_spread_price * contracts < current_balance - 2000:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 20000 and current_balance < 50000:
            if debit_spread_price * contracts < current_balance - 5000:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 50000 and current_balance < 100000:
            if debit_spread_price * contracts < current_balance - 10000:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 100000 and current_balance < 200000:
            if debit_spread_price * contracts < current_balance - 20000:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 200000 and current_balance < 500000:
            if debit_spread_price * contracts < current_balance - 50000:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 500000 and current_balance < 1000000:
            if debit_spread_price * contracts < current_balance - 100000:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1
        elif current_balance >= 1000000:
            if debit_spread_price * contracts < current_balance - 200000:
                contracts += 1
            else:
                contracts -= 1
                date += timedelta(days=7)
                s = date.strftime("%Y%m%d")
                date_list.append(s)
                profit = (100.0 - debit_spread_price) * contracts
                current_balance += profit
                profit_list.append(profit)
                balance_list.append(current_balance)
                contract_list.append(contracts)
                m += 1


    table.append(date_list)
    table.append(balance_list)
    table.append(profit_list)
    table.append(contract_list)

    workbook = xlsxwriter.Workbook('debit_spread_calculator.xlsx')
    worksheet = workbook.add_worksheet()

    for x in range(4):
        worksheet.write_column(0, x, table[x])
    workbook.close()

    return table

# def specific_calculator(current_balance, profit, debit_spread_price, contracts, profit_list, balance_list, contract_list):
#     profit = (100.0 - debit_spread_price) * contracts
#     current_balance += profit
#     profit_list.append(profit)
#     balance_list.append(current_balance)
#     contract_list.append(contracts)


ds_calculator("20200814", 200.0, 20, 75.0)



