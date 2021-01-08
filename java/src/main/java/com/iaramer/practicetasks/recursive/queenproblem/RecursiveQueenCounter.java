package com.iaramer.practicetasks.recursive.queenproblem;

public class RecursiveQueenCounter {
    int n;
    int queenPlacementVariations = 0;
    int queensQuantity;
    int[][] board;
    private int underAttack = 1;
    private int queen = 8;

    public static void main(String[] args) {
        int n = 5;
//        int n = Integer.parseInt(args[0]);
        RecursiveQueenCounter advRecursiveQueenCounter = new RecursiveQueenCounter(n);
        System.out.println("VARIATIONS: " + advRecursiveQueenCounter.count());
    }

    public RecursiveQueenCounter(int n) {
        this.n = n;
        queensQuantity = n;
        board = new int[n][n];
    }

    private boolean isEmptyAndSafeCell(int cell) {
        return cell == 0;
    }

    private void drawBoard(int[][] board) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) System.out.printf("%1$2s ", "_");
                if (board[i][j] == 1) System.out.printf("%1$2s ", "x");
                if (board[i][j] == 8) System.out.printf("%1$2s ", "@");
//                System.out.printf("%1$2d ", board[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }

    private void attackCells(int[][] changedBoard, int row, int column) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == row || j == column
                        || (i - j == row - column) || (i + j == row + column)) {
                    if (isEmptyAndSafeCell(changedBoard[i][j])) {
                        changedBoard[i][j] = underAttack;
                    }
                }
            }
        }
    }

    private int[][] cloneBoard(int[][] oldBoard) {
        int[][] newBoard = oldBoard.clone();
        for (int i = 0; i < oldBoard.length; i++)
            newBoard[i] = oldBoard[i].clone();
        return newBoard;
    }

    public int count() {
        for (int i = 0; i < n; i++) {
            recursivelyCount(queensQuantity, board, i);
        }
        return queenPlacementVariations;
    }

    private void recursivelyCount(int queensLeft, int[][] board, int rowToStartWith) {

        int column = n - queensLeft;
        int row = rowToStartWith;
        int[][] changedBoard = cloneBoard(board);

//        System.out.println("Q: " + queensLeft + "; Row: " + (row + 1) + "; Column: " + (column + 1));
//        drawBoard(board);

        if (queensLeft == 1 && isEmptyAndSafeCell(changedBoard[row][column])) {
            changedBoard[row][column] = queen;
            attackCells(changedBoard, row, column);
            queenPlacementVariations += 1;
            System.out.println("VARIATION №" + queenPlacementVariations);
            drawBoard(changedBoard);
        } else if (row < n && column < n && isEmptyAndSafeCell(changedBoard[row][column])) {
            changedBoard[row][column] = queen;
            attackCells(changedBoard, row, column);
            for (int i = 0; i < n; i++) {
                recursivelyCount(queensLeft - 1, changedBoard, i);
            }
        }
    }
}
