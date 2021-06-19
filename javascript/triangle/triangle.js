export class Triangle {
  constructor(...sides) {
    this.sides = sides;
  }

  get isEquilateral() {
    if (!Triangle.isValidTriangle(this.sides)) return false;
    return this.sides[0] === this.sides[1] && this.sides[1] === this.sides[2];
  }

  get isIsosceles() {
    if (!Triangle.isValidTriangle(this.sides)) return false;
    return this.sides[0] === this.sides[1] || this.sides[0] === this.sides[2] || this.sides[1] === this.sides[2];
  }

  get isScalene() {
    if (!Triangle.isValidTriangle(this.sides)) return false;
    return this.sides[0] !== this.sides[1] && this.sides[1] !== this.sides[2] && this.sides[2] !== this.sides[0];
  }

  static isValidTriangle(sides) {
    let sidesGreaterThanZero = sides.every(side => side > 0);
    const pairings = [[0, 1, 2], [1, 2, 0], [2, 0, 1]];
    let inequality = pairings.every(pairing => {
      return (sides[pairing[0]] + sides[pairing[1]]) >= sides[pairing[2]]
    });
    return sidesGreaterThanZero && inequality;
  }
}
