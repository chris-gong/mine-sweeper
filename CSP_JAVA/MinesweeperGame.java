package minesweeper;

//import java.util.Arrays;
import java.util.Random;

public class MinesweeperGame {

	public static int height;
	public static int width;

	public static int[][] getGrid(int bombs) {
		Random random = new Random();
		int[][] grid = new int[height][width];
		int occupiedSpots = 0;
		
		while (occupiedSpots < bombs) {
			int x = random.nextInt(height);
			int y = random.nextInt(width);
			
			if (grid[x][y] == 0) {
		    	grid[x][y] = 9;
		    	occupiedSpots = occupiedSpots + 1;
		    }
		}
		
		for (int x = 0; x < grid.length; x++) {
			for (int y = 0; y < grid[x].length; y++) {
				if (grid[x][y] != 9) {
					grid[x][y] = getAdjacentCount(grid, x, y);
				}
			}
		}
		
		return grid;
	}
	
	public static boolean isValid(int x, int y) {
		if ((x < 0 || x > height - 1) || (y < 0 || y > width - 1)) {
			return false;
		}
		else {
			return true;
		}
	}
	
	public static int getAdjacentCount(int[][] grid, int x, int y) {
		int count = 0;
		
		if (isValid(x-1, y-1)) {
			if (grid[x-1][y-1] == 9) {
				count = count + 1;
			}
		}
		if (isValid(x-1, y)) {
			if (grid[x-1][y] == 9) {
				count = count + 1;
			}
		}
		if (isValid(x-1, y+1)) {
			if (grid[x-1][y+1] == 9) {
				count = count + 1;
			}
		}
		if (isValid(x, y-1)) {
			if (grid[x][y-1] == 9) {
				count = count + 1;
			}
		}
		if (isValid(x, y+1)) {
			if (grid[x][y+1] == 9) {
				count = count + 1;
			}
		}
		if (isValid(x+1, y-1)) {
			if (grid[x+1][y-1] == 9) {
				count = count + 1;
			}
		}
		if (isValid(x+1, y)) {
			if (grid[x+1][y] == 9) {
				count = count + 1;
			}
		}
		if (isValid(x+1, y+1)) {
			if (grid[x+1][y+1] == 9) {
				count = count + 1;
			}
		}
		
		return count;
	}
}