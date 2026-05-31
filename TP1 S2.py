# ex1
def power(base,expo=2):
    if expo < 0:
        return 1/(base**abs(expo)) 
    else:
        return base ** expo
f1 =power
print(f1(1)) # o(1)

def scale( x, factor=1.2):
    if x == 0:
        return 0
    else:
        return x * factor
f2 = scale
print(f2(10)) # o(1)

# ex2
def apply_all(funcs,value):
    res = []
    for i in funcs:
        res.append(i(value))
    return res
print(apply_all([f1,f2],10)) # o(n) because we iterate through the list of functions once, where n is the number of functions in the list. Each function application is O(1), so the overall complexity is O(n).

#ex3
def summarize(*args, **kwargs):
    if len(args) == 0:
        return None
    total = sum(args)
    average = total / len(args)
    
    precision = kwargs.get('precision', 2)
    verbose = kwargs.get('verbose', False)
    
    average_rounded = round(average, precision)
    total_rounded = round(total, precision)
    
    if verbose:
        print("=" * 10)
        print("SUMMARY REPORT")
        print("=" * 10)
        print(f"Numbers: {args}")
        print(f"Count: {len(args)} numbers")
        print(f"Sum: {total_rounded} (rounded to {precision} decimals)")
        print(f"Average: {average_rounded} (rounded to {precision} decimals)")
        print("=" * 10)
    
    return (total_rounded, average_rounded)
print(summarize(1, 2, 3, precision=3, verbose=False))
print(summarize(5,10,15 ,verbose=True))
print(summarize())