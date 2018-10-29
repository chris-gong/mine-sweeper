/**
 * Main player of MineSweeper game with automation for cell queries.
 */

package minesweeper;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

public class MinesweeperPlayer_auto {

	private static List<Constraint> constraints;
	private static List<Variable> masterVariables;
	private static List<Variable> unTraversedTiles;
	private static Queue<Coordinate> fringe;
	private static char[][] player;
	private static int height;
	private static int width;

	public static void main(String[] args) {
		// Initialize variables
		Random random = new Random();
		Scanner scanner = new Scanner(System.in);
		constraints = new ArrayList<Constraint>();
		masterVariables = new ArrayList<Variable>();
		unTraversedTiles = new ArrayList<Variable>();

		// Ask for user input
		System.out.println("Welcome to AI player!");
		System.out.println("Please enter the height: ");
		height = scanner.nextInt();
		System.out.println("Please enter the width: ");
		width = scanner.nextInt();
		System.out.println("Please enter # of bombs: ");
		int bombs = scanner.nextInt();

		// Simple dimension check
		if (height < 2 || width < 2 || bombs >= width * height) {
			System.out.print("ERROR: dimension and/or bombs");
			System.exit(0);
		}

		// Create master grid
		MinesweeperGame.height = height;
		MinesweeperGame.width = width;
		int[][] master = MinesweeperGame.getGrid(bombs);

		// Print master grid
		System.out.println("\nMaster Grid: ");
		for (int x = 0; x < master.length; x++) {
			System.out.println(Arrays.toString(master[x]));
		}

		// Create player grid
		player = new char[height][width];
		for (int x = 0; x < player.length; x++) {
			for (int y = 0; y < player[x].length; y++) {
				player[x][y] = '-';
			}
		}

		// Print player grid
		System.out.println("\nPlayer Grid: ");
		for (int x = 0; x < player.length; x++) {
			System.out.println(Arrays.toString(player[x]));
		}

		// Create non-traversed list of tiles
		for (int x = 0; x < height; x++) {
			for (int y = 0; y < width; y++) {
				unTraversedTiles.add(new Variable(x, y, null));
			}
		}

		// Guess corner tile first and add to fringe.
		// Based on MineSweeper strategy of choosing corners first since they have lowest probability of having a mine
		fringe = new LinkedList<Coordinate>();
		fringe.add(new Coordinate((random.nextInt() % 2 == 0) ? 0 : height - 1, (random.nextInt() % 2 == 0) ? 0 : width - 1, 1.0));

		// The main loop, while fringe is empty or all tiles have not been mined
		while (fringe.size() > 0 || masterVariables.size() < width * height) {
			int row;
			int col;
			Coordinate tile;
			// If fringe is not empty, pick a clear cell to traverse
			if (fringe.size() > 0) {
				System.out.println("\n-----------------");
				System.out.println("Current Fringe: " + fringe);
				tile = fringe.poll();
				row = tile.x;
				col = tile.y;
				System.out.println("AI chose clear cell: [" + row + ", " + col + "]: ");
			}
			else {
				// If fringe is empty and constraints is empty, pick a random untraversed tile (mines are blocking view)
				if (constraints.size() == 0) {
					unTraversedTiles.removeAll(masterVariables);
					Variable tempVar = unTraversedTiles.get((int) Math.floor(Math.random()*unTraversedTiles.size()));
					row = tempVar.row;
					col = tempVar.col;
					unTraversedTiles.remove(tempVar);
					System.out.println("\n-----------------");
					System.out.println("Current Fringe: " + fringe);
					System.out.println("Since no knowledge of board, AI chose random cell: [" + row + ", " + col + "]: ");
				}
				// If fringe is empty and constraints is not empty, make an educated guess.
				else {
					List<Coordinate> possible = new ArrayList<Coordinate>();
					for (int x = 0; x < constraints.size(); x++) {
						for (int y = 0; y < constraints.get(x).LHS.size(); y++) {
							possible.add(new Coordinate(constraints.get(x).LHS.get(y).row, constraints.get(x).LHS.get(y).col, (1.0 - (double)constraints.get(x).RHS/(double)constraints.get(x).getSize())));
						}
					}

					Collections.sort(possible);
					possible = new ArrayList<Coordinate>(new LinkedHashSet<Coordinate>(possible));
					int scale = (int) Math.pow(10, 2);
					double probability = (double) Math.round(possible.get(0).probability * scale) / scale;
					System.out.println(possible);
					unTraversedTiles.removeAll(masterVariables);
					
					if (possible.get(0).probability > 0.70) {
						int sameIndex = 0;
						for (int x = 1; x < possible.size(); x++) {
							if (possible.get(x).probability == possible.get(0).probability) {
								sameIndex = x;
							}
						}
						
						sameIndex = sameIndex + 1;
						Coordinate tempCor = possible.get((int) Math.floor(Math.random()*(sameIndex)));
						row = tempCor.x;
						col = tempCor.y;
						System.out.println("\n-----------------");
						System.out.println("Current Fringe: " + fringe);
						System.out.println("The AI is making a relatively safe move at: [" + row + ", " + col + "]... probability of success: " + probability + ".");
					}
					else {
						if (unTraversedTiles.size() == possible.size()) {
							System.out.println("Size of unTraversedTiles: " + unTraversedTiles.size());
							Variable tempVar = unTraversedTiles.get((int) Math.floor(Math.random()*unTraversedTiles.size()));
							row = tempVar.row;
							col = tempVar.col;
							unTraversedTiles.remove(tempVar);
							System.out.println("\n-----------------");
							System.out.println("Current Fringe: " + fringe);
							System.out.println("Since probability <= 0.7, AI chose random cell: [" + row + ", " + col + "]: ");
						}
						else {
							for (int x = 0; x < possible.size(); x++) {
								unTraversedTiles.remove(new Variable(possible.get(x).x, possible.get(x).y, null));
							}
							
							System.out.println("Size of unTraversedTiles: " + unTraversedTiles.size());
							Variable tempVar = unTraversedTiles.get((int) Math.floor(Math.random()*unTraversedTiles.size()));
							row = tempVar.row;
							col = tempVar.col;
							unTraversedTiles.remove(tempVar);
							System.out.println("\n-----------------");
							System.out.println("Current Fringe: " + fringe);
							System.out.println("Since probability <= 0.7, AI chose random cell: [" + row + ", " + col + "]: ");
							
							for (int x = 0; x < possible.size(); x++) {
								unTraversedTiles.add(new Variable(possible.get(x).x, possible.get(x).y, null));
							}
						}
					}
				}
			}
			
			// After row and col have been selected, check if AI selected a mine.
			if (master[row][col] == 9) {
				System.out.println("\nThe AI touched a mine at: [" + row + ", " + col + "]. Game over!");
				System.exit(0);
			}
			// The AI did not select a mine, therefore the cell is clear!
			else {
				player[row][col] = (char)(master[row][col] + '0');
				masterVariables.add(new Variable(row, col, 0));

				setConstraint(row, col, master[row][col]);
				Collections.sort(constraints);

				int sizeold;
				int sizenew;

				// Simplify constraints continuously until they are completely simplified
				do {
					sizeold = constraints.size();
					knownVariableCheck();
					subsetCheck();
					zeroAndOne();
					sizenew = constraints.size();
				} while (sizeold != sizenew);

				// Check for inconsistencies
				for (int x = 0; x < constraints.size(); x++) {
					if (constraints.get(x).getSize() < 1 || constraints.get(x).RHS < 0 || constraints.get(x).RHS > 8) {
						System.out.println("ERROR: inconsistent system");
						System.exit(0);
					}
				}

				// Print current state of player grid after AI's cell choice
				System.out.println("\nPlayer Grid: ");
				for (int x = 0; x < player.length; x++) {
					System.out.println(Arrays.toString(player[x]));
				}

				System.out.println("\nConstraints after Math: "+ constraints);
				masterVariables = new ArrayList<Variable>(new LinkedHashSet<Variable>(masterVariables));
				System.out.println("Known Variables List: " + masterVariables);
			}
		}

		// Check if AI's grid equals the master grid
		for (int x = 0; x < height; x++) {
			for (int y = 0; y < width; y++) {
				if ((Character.getNumericValue(player[x][y]) == master[x][y]) || (player[x][y] == 'M' && master[x][y] == 9)) {
					continue;
				}
				else {
					System.out.println("\nAI did not complete the game correctly!");
					System.exit(0);
				}
			}
		}

		// Print success
		System.out.println("\nAI successfully traversed the system!");

		scanner.close();
	}

	// Method that checks if subsets of constraints exists and substitutes them in parent constraint
	public static void subsetCheck() {
		for (int x = 0; x < constraints.size() - 1; x++) {
			for (int y = x + 1; y < constraints.size(); y++) {
				if (constraints.get(y).LHS.containsAll(constraints.get(x).LHS)) {
					constraints.get(y).LHS.removeAll(constraints.get(x).LHS);
					constraints.get(y).RHS = constraints.get(y).RHS - constraints.get(x).RHS;
				}
			}
		}
	}

	// Method that replaces variables in constraints to known variables in masterVariables list
	public static void knownVariableCheck() {
		for (int x = 0; x < constraints.size(); x++) {
			for (int y = 0; y < constraints.get(x).LHS.size(); y++) {
				if (masterVariables.contains(constraints.get(x).LHS.get(y))) {
					constraints.get(x).RHS = constraints.get(x).RHS - masterVariables.get(masterVariables.indexOf(constraints.get(x).LHS.get(y))).value;
					constraints.get(x).LHS.remove(y);
				}
			}
		}
	}

	// Method that checks if constraints are simple enough to confirm clear or mine cells
	public static void zeroAndOne() {
		for (int x = 0; x < constraints.size(); x++) {
			if (constraints.get(x).RHS == 0) {
				for (int y = 0; y < constraints.get(x).LHS.size(); y++) {
					masterVariables.add(new Variable(constraints.get(x).LHS.get(y).row, constraints.get(x).LHS.get(y).col, 0));
					fringe.add(new Coordinate(constraints.get(x).LHS.get(y).row, constraints.get(x).LHS.get(y).col, 1.0));
					player[constraints.get(x).LHS.get(y).row][constraints.get(x).LHS.get(y).col] = 'C';
				}
				constraints.remove(x);
				x = x - 1;
			}
			else if (constraints.get(x).LHS.size() == constraints.get(x).RHS) {
				for (int y = 0; y < constraints.get(x).LHS.size(); y++) {
					masterVariables.add(new Variable(constraints.get(x).LHS.get(y).row, constraints.get(x).LHS.get(y).col, 1));
					player[constraints.get(x).LHS.get(y).row][constraints.get(x).LHS.get(y).col] = 'M';
				}
				constraints.remove(x);
				x = x - 1;
			}
		}
	}

	// Sets constraints by getting all valid neighboring cells and setting the RHS to clue cell value
	public static void setConstraint(int x, int y, int value) {
		int RHS = value;
		List<Variable> LHS = new ArrayList<Variable>();

		//N
		if (isValid(x-1, y)) {
			Variable variableTemp = new Variable(x-1, y, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}
		//W
		if (isValid(x, y-1)) {
			Variable variableTemp = new Variable(x, y-1, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}
		//E
		if (isValid(x, y+1)) {
			Variable variableTemp = new Variable(x, y+1, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}
		//S
		if (isValid(x+1, y)) {
			Variable variableTemp = new Variable(x+1, y, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}
		//NW
		if (isValid(x-1, y-1)) {
			Variable variableTemp = new Variable(x-1, y-1, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}
		//NE
		if (isValid(x-1, y+1)) {
			Variable variableTemp = new Variable(x-1, y+1, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}
		//SW
		if (isValid(x+1, y-1)) {
			Variable variableTemp = new Variable(x+1, y-1, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}
		//SE
		if (isValid(x+1, y+1)) {
			Variable variableTemp = new Variable(x+1, y+1, null);
			if (!(masterVariables.contains(variableTemp))) {
				LHS.add(variableTemp);
			}
			else {
				RHS = RHS - masterVariables.get(masterVariables.indexOf(variableTemp)).value;
			}
		}

		if (LHS.size() != 0) {
			constraints.add(new Constraint(LHS, RHS));
		}
	}

	// Checks if a row and col value are valid for the grid
	public static boolean isValid(int x, int y) {
		if ((x < 0 || x > height - 1) || (y < 0 || y > width - 1)) {
			return false;
		}
		else {
			return true;
		}
	}
}