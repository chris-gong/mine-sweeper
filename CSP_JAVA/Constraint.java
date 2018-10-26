package minesweeper;

import java.util.List;

public class Constraint implements Comparable<Constraint> {
	public List<Variable> LHS;
	public int RHS;

	public Constraint(List<Variable> LHS, int RHS) {
		this.LHS = LHS;
		this.RHS = RHS;
	}

	public String toString() {
		String toPrint = "";
		for (int x = 0; x < LHS.size() - 1; x++) {
			toPrint = toPrint + LHS.get(x) + " + ";
		}
		
		toPrint = toPrint + LHS.get(LHS.size() - 1);
		
		toPrint = toPrint + " = " + RHS;
		return toPrint;
	}

	public int getSize() {
		return LHS.size();
	}

	public int compareTo(Constraint c) {
		if (this.getSize() > c.getSize()) {
			return 1;
		}
		else if (this.getSize() < c.getSize()) {
			return -1;
		}
		else {
			return 0;
		}
	}
}