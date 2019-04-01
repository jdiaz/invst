#!/usr/bin/env python3

import math

class InvestmentCalculator:

    def set_stock_price(self, stock_price):
        self.stock_price = stock_price
        return self


    def set_payout_period(self, time_period = 4):
        self.payout_period = time_period
        return self

    
    def set_payout_ratio(self, payout_ratio):
        self.payout_ratio = payout_ratio
        return self

    
    def set_investment_per_payout_period(self, payment):
        self.investment_per_payout_period = payment
        return self


    def set_shares(self, shares):
        self.total_shares = shares
        return self


    def set_years(self, yrs):
        self.years = yrs
        return self


    def set_year_percentage_return(self, ret):
        self.year_return = ret
        return self


    def should_reinvest_dividends(self, reinvest):
        self.reinvest_dividends = reinvest
        return self


    def __format_money(self, money):
        return '${:,.2f}'.format(money)


    def __stock_value(self, stock_price, number_of_stocks):
        return self.__format_money(number_of_stocks * stock_price)


    def __dividend_payout(self, shares, payout_ratio):
        frac_shares, whole_shares = math.modf(shares) # separate decimal portion of shares you own
        return whole_shares * payout_ratio + frac_shares * payout_ratio
        

    def __purchasable_stock_amount(self, stock_price, money):
        if money == 0:
            return 0
        return money / stock_price


    def compute(self):
        print('=========================================================================================')
        print('Investment analysis:')
        print('\tFor {} years'.format(self.years))
        print('\tStarting shares: {}, {}'.format(self.total_shares, self.__format_money(self.total_shares * self.stock_price)))
        print('\tStarting stock price: {}'.format(self.__format_money(self.stock_price)))
        print('\tInvesting {} per pay period ({}) times a year'.format(self.investment_per_payout_period, self.payout_period))
        print('\tResults:')
        total_money_from_divided_payout = 0
        for _ in range(self.years):
            for _ in range(self.payout_period):
                money_made_from_dividend = self.__dividend_payout(self.total_shares, self.payout_ratio)
                total_money_from_divided_payout += money_made_from_dividend
                if self.reinvest_dividends:
                    stock_purchased_from_dividends = self.__purchasable_stock_amount(self.stock_price, money_made_from_dividend)
                    self.total_shares += stock_purchased_from_dividends
                self.total_shares += self.__purchasable_stock_amount(self.stock_price, self.investment_per_payout_period)
            # Increase stock price by Year Return %; once every year
            self.stock_price += (self.stock_price * self.year_return)
            
        print('\tTotal stock: {}, {}'.format(self.total_shares, self.__stock_value(self.stock_price, self.total_shares)))
        print('\tNew stock price: {}'.format(self.__format_money(self.stock_price)))
        print('\tTotal made from dividends: {}, Was it reinvested? {}'.format(self.__format_money(total_money_from_divided_payout), self.reinvest_dividends))
        print('\tGoing forward per quarter you will make: {}'.format(self.__format_money(self.total_shares * self.payout_ratio)))

global_years = 5
global_investment_per_period = 4000

def calculateATTStock():
    """
        Calculates stock investment in At&t stock
    """
    (InvestmentCalculator()) \
        .set_stock_price(31.07) \
        .set_shares(80) \
        .set_payout_period(4) \
        .set_investment_per_payout_period(global_investment_per_period) \
        .set_years(global_years) \
        .set_payout_ratio(0.51) \
        .set_year_percentage_return(0.0) \
        .should_reinvest_dividends(True) \
        .compute()
    
def calculateIVVFund():
    """
        Calculates stock investment in IVV ETF
    """
    (InvestmentCalculator()) \
        .set_stock_price(284.56) \
        .set_shares(20) \
        .set_payout_period(4) \
        .set_investment_per_payout_period(global_investment_per_period) \
        .set_years(global_years) \
        .set_payout_ratio(1.14) \
        .set_year_percentage_return(.1012) \
        .should_reinvest_dividends(False) \
        .compute()

if __name__ == '__main__':
    calculateATTStock()
    calculateIVVFund()