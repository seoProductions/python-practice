''' 

Feb 2024
Another python exercize to familiarize myself with python. Itsbeen a few years...
Write a program that reads an unspecified number of integers, determines how many positive and negative values have been read, and computes the total and average of the input values (not counting zeros). Your program ends with the input 0 . Display the average as a floating-point number. Here is a sample run:
'''

### Eliseo Duque
### Jan 25 2025


def main():
    prompt = "Enter an integer, the input ends if it is 0: "
    n = -1
    list = []


    while n != 0:
        n = int(input(prompt))
        list.append(n)

    if len(list) == 1:  # 0 only
        print("You didn't enter any number")
        return

    sum         = 0
    neg_count   = 0
    pos_count   = 0
    
    
    for i in list:
        if i < 0:
            neg_count += 1
        elif i > 0:
            pos_count += 1
        else:
            # zero found
            break
        sum += i
    
    #computer average
    average     = float(sum) / ( len(list) - 1 ) #omit 0

    #format output
    print("The number of positives is " + str(pos_count))
    print("The number of negatives is " + str(neg_count))
    print("The total is " + str(sum))
    print("The average is " + str(average))


main()
