/**
 * Class that represents a variable object.
 */

package minesweeper;

public class Variable {
	public int row;
	public int col;
	public Integer value;
	
	public Variable(int row, int col, Integer value) {
		this.row = row;
		this.col = col;
		this.value = value;
	}
	
	@Override
	public boolean equals(Object other){
		if (!(other instanceof Variable))
			return false;
		Variable otherVariable = (Variable) other;
		return (this.row==otherVariable.row) && (this.col == otherVariable.col) && 
				(this.getClass().getName().equals(otherVariable.getClass().getName()));
	}

	@Override
	public int hashCode() {
		int hash = 3;
		hash = 53 * hash + this.row;
		hash = 53 * hash + this.col;
		return hash;
	}
	
	public String toString() {
		return "[x: " + this.row + ", y: " + this.col + ", value: " + this.value + "]";
	}
}