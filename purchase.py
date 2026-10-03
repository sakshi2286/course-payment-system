# ========================================================
# 🏢 PROJECT: E-LEARNING COURSE PURCHASE SIMULATOR
# 💻 ROLE: BACKEND DEVELOPER (CORE TRANSACTION LOGIC)
# ========================================================

def process_purchase():
    print("\n" + "="*50)
    print("      🚀 CORE E-LEARNING PAYMENT SYSTEM 🚀      ")
    print("="*50)
    
    # 1. Mock Database Data (Course Details)
    course_name = "Advanced Premium Software Batch"
    course_price = 2999.00
    
    print(f"Target Course: {course_name}")
    print(f"Course Price: ${course_price}")
    print("-"*50)
    
    # 2. Student Input (Simulating App Requests)
    try:
        student_name = "Priyanka Kumari"
        student_balance = 5000.00
        
        print(f"Student Name: {student_name}")
        print(f"Student Bank Account Balance ($): {student_balance}")
        print("\n⏳ Processing transaction securely with Bank Servers...")
        
        # 3. Backend Logic: Check if funds are sufficient
        if student_balance >= course_price:
            # Deducting the course price from balance
            remaining_balance = student_balance - course_price
            
            # Success Trigger
            print("\n" + "*"*50)
            print("🎉 TRANSACTION SUCCESSFUL!")
            print("*"*50)
            print(f"Status: '{course_name}' has been unlocked for {student_name}.")
            print(f"Receipt: ${course_price} deducted.")
            print(f"Updated Wallet Balance: ${remaining_balance:,.2f}")
            print("✉️ Auto-Notification: Confirmation email sent to student.")
            print("*"*50 + "\n")
            
        else:
            # Error Handling for Insufficient Funds
            shortage = course_price - student_balance
            print("\n" + "❌"*20)
            print("❌ TRANSACTION FAILED: Insufficient Funds!")
            print("❌"*20)
            print(f"Reason: {student_name} needs ${shortage:,.2f} more to buy this batch.")
            print("⚠️ Action: Prompting user to try another payment method.")
            print("❌"*20 + "\n")
            
    except ValueError:
        print("\n❌ System Error: Invalid balance amount entered. Please enter numbers only.")

# Run the simulator
if __name__ == "__main__":
    process_purchase()