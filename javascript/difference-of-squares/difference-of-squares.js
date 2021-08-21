export class Squares {
  constructor(n) {
    this.vals = [];
    for (let i = 1; i <= n; i += 1) {
      this.vals.push(i);
    }
  }

  get sumOfSquares() {
    let sum = 0;
    for (let i = 0; i < this.vals.length; i += 1) {
      sum += this.vals[i] * this.vals[i];
    }
    return sum;
  }

  get squareOfSum() {
    let sum = 0;
    for (let i = 0; i < this.vals.length; i += 1) {
      sum += this.vals[i];
    }
    return sum * sum;
  }

  get difference() {
    return this.squareOfSum - this.sumOfSquares;
  }
}
