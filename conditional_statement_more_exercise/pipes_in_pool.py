pool_volume = float(input())
debit_pipe_one = float(input())
debit_pipe_two = float(input())
missing_hours = float(input())

debit_pipe_one_missing_time = missing_hours * debit_pipe_one
debit_pipe_two_missing_time = missing_hours * debit_pipe_two
total_debit = debit_pipe_one_missing_time + debit_pipe_two_missing_time

percent_debit_pipe_one = (debit_pipe_one_missing_time * 100) / total_debit
percent_debit_pipe_two = (debit_pipe_two_missing_time * 100) / total_debit

total_filling_percent = (total_debit * 100 ) / pool_volume

if pool_volume >= total_debit:
    print(f'The pool is {total_filling_percent}% full. Pipe 1: {percent_debit_pipe_one:.2f}%. Pipe 2: {percent_debit_pipe_two:.2f}%.')

elif total_debit > pool_volume:
    quantity_out = total_debit - pool_volume
    print(f'For {missing_hours} hours the pool overflows with {quantity_out} liters.')