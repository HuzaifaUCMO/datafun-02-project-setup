import statistics

''' Module: Quantum Insights - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.
'''

is_remote_friendly: bool = True
number_of_clients: int = 50
services_offered: list = ["Data Visualization", "Machine Learning", "Statistical Analysis"]
client_satisfaction_scores: list = [4.5, 4.7, 4.8, 5.0, 3.9, 4.2]

byline: str = f'''Quantum Insights: Delivering Actionable Intelligence
- Remote Friendly: {is_remote_friendly}
- Clients Served: {number_of_clients}
- Services: {', '.join(services_offered)}
- Avg. Client Satisfaction: {statistics.mean(client_satisfaction_scores):.2f}
- Client Satisfaction Std Dev: {statistics.stdev(client_satisfaction_scores):.2f}'''

def get_byline() -> str:
    '''Returns the byline string.'''
    return byline

def print_statistics() -> None:
    '''Calculates and prints statistics for client satisfaction scores.'''
    print(f'Minimum Score: {min(client_satisfaction_scores)}')
    print(f'Maximum Score: {max(client_satisfaction_scores)}')
    print(f'Average Score: {statistics.mean(client_satisfaction_scores)}')
    print(f'Standard Deviation: {statistics.stdev(client_satisfaction_scores)}')

def main() -> None:
    '''Print the byline and statistics.'''
    print(get_byline())
    print_statistics()

if __name__ == '__main__':
    main()
