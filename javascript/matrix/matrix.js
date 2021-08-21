export class Matrix {
  constructor(string) {
    let arr = string.split('\n');
    this.matrixRows = arr.map(row => {
      return row.split(" ").map(val => Number(val));
    });

    this.matrixColumns = [];
    let maxRowLength = this.maxRowLength();
    for (let col = 0; col < maxRowLength; col += 1) {
      let column = [];
      for (let row = 0; row < this.matrixRows.length; row += 1) {
        let val = this.matrixRows[row][col];
        column.push(val);
      }
      this.matrixColumns.push(column);
    }
  }

  get rows() {
    return this.matrixRows;
  }

  get columns() {
    return this.matrixColumns;
  }

  maxRowLength() {
    let max = 0;
    this.matrixRows.forEach(row => {
      if (row.length > max) {
        max = row.length;
      }
    });
    return max;
  }
}
