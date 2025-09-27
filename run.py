from waterfall.main import get_context_summary

query = input("Enter the topic whose context you want: ")
context = get_context_summary(query)
print(context)