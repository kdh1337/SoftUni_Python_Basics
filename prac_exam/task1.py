movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_cut = int(input())

money_from_tickets = days * tickets * ticket_price
profit_for_studio = money_from_tickets * (cinema_cut / 100)
profit_for_cinema = money_from_tickets - profit_for_studio

print(f'The profit from the movie {movie_name} is {profit_for_cinema:.2f} lv.')