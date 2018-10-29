/**
 * Class that represents a coordinate object.
 */

package minesweeper;

public class Coordinate implements Comparable<Coordinate> {
	public int x;
	public int y;
	public double probability;
	
	public Coordinate(int x, int y, double probability) {
		this.x = x;
		this.y = y;
		this.probability = probability;
	}
	
	public String toString() {
		return "x: " + x + ", y: " + y + ", prob: " + probability;
	}
	
	public int compareTo(Coordinate c) {
		if (this.probability < c.probability) {
			return 1;
		}
		else if (this.probability > c.probability) {
			return -1;
		}
		else {
			return 0;
		}
	}
	
	@Override
	public boolean equals(Object other){
		if (!(other instanceof Coordinate))
			return false;
		Coordinate otherCoordinate = (Coordinate) other;
		return (this.x==otherCoordinate.x) && (this.y == otherCoordinate.y) && 
				(this.getClass().getName().equals(otherCoordinate.getClass().getName()));
	}
	
	@Override
	public int hashCode() {
		int hash = 3;
		hash = 53 * hash + this.x;
		hash = 53 * hash + this.y;
		return hash;
	}
}