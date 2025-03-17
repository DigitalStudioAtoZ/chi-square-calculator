from scipy.stats import chi2

def chi_square_right_tail():
    try:
        # Get user input for degrees of freedom
        df = int(input("Enter degrees of freedom (df): "))
        if df <= 0:
            print("Degrees of freedom must be a positive integer.")
            return
        
        # Get user input for chi-square test statistic
        x = float(input("Enter the chi-square test statistic (x): "))
        if x < 0:
            print("Chi-square statistic (x) must be non-negative.")
            return

        # Compute the right-tail probability P(χ² > x)
        probability = 1 - chi2.cdf(x, df)

        # Display result
        print(f"\nP(χ² > {x}) = {probability:.4f}")

    except ValueError:
        print("Invalid input! Please enter numerical values for df and x.")

# Run the function
chi_square_right_tail()

# run this code on any pythode code runner
