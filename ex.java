import java.util.*;
public class ex{
    int n;
    void print_board(int board[][]){
        System.out.println("Solution");
        for(int row=0;row <n;row++){
            for(int col=0;col<n;col++){
                if(board[row][col]==1){
                    System.out.print(" Q ");

                }
                else{
                    System.out.print(" . ");
                }
                
            }
            System.out.println();
        }
    }
    boolean is_safe(int board[][],int row ,int col){
        for(int i=0;i<col;i++){
            if(board[row][i]==1){
                return false;
            }
        }
        for(int i=row,j=col;i>=0 && j>=0;i--,j--){
            if(board[i][j]==1){
                return false;
            }
        }
        for(int i=row,j=col;i<n && j>=0; i++,j--){
            if(board[i][j]==1){
                return false;
            }
        }
    return true;

    }
    boolean backtrack(int board[][],int col){
        if(col>=n){
            print_board(board);
            return true;
        }
        for(int row=0;row<n; row++){
            if (is_safe(board,row,col)){
                board[row][col]=1;
            
            if(backtrack(board,col+1)){
             return true;
            }
            board[row][col]=0;
            }
        }
        return false;

    }
    boolean [] usedRows;
    boolean [] usedUpperDiagonal;
    boolean [] usedLowerDiagonal;
    boolean branchnbound(int board[][],int col){
        if(col>=n){
            print_board(board);
            return true;
        }
        for(int row=0;row<n;row++){
            int upperdig =row+col;
            int lowerdig=row-col+n-1;
            if(!usedRows[row]&& 
            !usedUpperDiagonal[upperdig]
            && !usedLowerDiagonal[lowerdig]){
                board[row][col]=1;
                usedRows[row]=true;
                usedUpperDiagonal[upperdig]=true;
                usedLowerDiagonal[lowerdig]=true;
                if(branchnbound(board, col+1)){
                    return true;
                }
                board[row][col]=0;
                usedRows[row]=false;
                usedUpperDiagonal[upperdig]=false;
                usedLowerDiagonal[lowerdig]=false;
            }
        }
        return false;

    }
    void solve(){
        Scanner sc=new Scanner(System.in);
        System .out.print("Enter value of n:");
        n=sc.nextInt();
        int board[][]=new int[n][n];
        System.out.println("1 Backtracking");
        System.out.println(" 2.Branch an dbound");
        System.out.print("Enetr your choice");
        int choice=sc.nextInt();
        if (choice == 1) {
            boolean answer =
            backtrack(board, 0);
            if (!answer) {
                System.out.println("No solution exists");
            }
        }
        else if (choice == 2) {
            usedRows =new boolean[n];
            usedUpperDiagonal =new boolean[2 * n- 1];
                usedLowerDiagonal =new boolean[2 * n - 1];
            boolean answer =branchnbound(board, 0);
            if (!answer) {
                System.out.println("No solution exists");
            }
        }
        else{ System.out.println("Invalid choice");

        }

    }
   public static void main(String [] args){
        ex obj=new ex();
        obj.solve();
    }
}


