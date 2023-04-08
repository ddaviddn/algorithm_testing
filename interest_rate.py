from typing import Any


def investment_calc(start_investment: int,
                    rate_of_return: float,
                    rate_of_inflation: float,
                    years_invested: int,
                    withdrawals: int) -> list[int | Any]:
    """
    This function will return the investment after the inputted
    number of years invested. This is useful for financial managers
    when doing financial planning.
    :param start_investment: Investment started with.
    :param rate_of_return: Rate of return on the investment account.
    :param rate_of_inflation: Rate of inflation, set at market level.
    :param years_invested: Years kept into investment account.
    :param withdrawals: The amount withdrawn each year.
    :return: Expected balance of account.
    """

    investment_history = [start_investment]

    for years in range(years_invested):
        next_year = (investment_history[years] + (investment_history[years] * rate_of_return)) - \
                    (investment_history[years] * rate_of_inflation) - withdrawals
        investment_history.append(round(next_year, 3))

    return investment_history[-1]


if __name__ == "__main__":
    initial_investment = 100000
    interest_rate = 1.01
    inflation_rate = 1.011
    n_years = 12

    for i in ((1000, 2000), (3000, 5000), (9000, 10000), (20000, 40000)):
        investments_lb = investment_calc(initial_investment,
                                         interest_rate,
                                         inflation_rate,
                                         n_years,
                                         i[0])
        investments_ub = investment_calc(initial_investment,
                                         interest_rate,
                                         inflation_rate,
                                         n_years,
                                         i[1])

        print("-"*40)
        print(f"The investment for pulling {i[0]} is: {investments_lb}")
        print(f"The investment for pulling {i[1]} is: {investments_ub}")