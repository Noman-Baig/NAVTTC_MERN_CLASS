class BankAccount {
  constructor(owner, balance = 0) {
    this.owner = owner;
    this.balance = balance;
  }

  deposit(amount) {
    this.balance += amount;
    console.log(`Deposited ${amount}. New balance: ${this.balance}`);
  }

  withdraw(amount) {
    if (amount > this.balance) {
      console.log("Insufficient funds ");
    } else {
      this.balance -= amount;
      console.log(`Withdrew ${amount}. New balance: ${this.balance}`);
    }
  }
}

// Create an object (instance)
const account = new BankAccount("Ali", 1000);

// Call methods on the object
account.deposit(500);
account.withdraw(300);
account.withdraw(1500);
