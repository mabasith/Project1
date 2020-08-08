#include<iostream>
#include<string>
#include <stdio.h>
#include <cstring>

using namespace std;

class Board
{
  char positionsSelected[16];
  char winner;
  
  public:
  Board()
  {
      winner = 'z';
      for(int i = 0; i < 16; i++)
      {
          positionsSelected[i] = '_';
      }
      
  }
  
  char* getPositions(void)
  {
      return positionsSelected;
  }
  
  int setPosition(int gridNumber, char user)
  {
      if(positionsSelected[gridNumber] == '_')
      {
          positionsSelected[gridNumber] = user;
          return 0;
      }
      else
      {
          return -1;
      }
      
  }
  char checkRows()
  {
      int fourInRowX = 0;
      int fourInRowO = 0;
      for(int row = 0; row < 16; row = row + 4)
      {
          for(int i=0; i < 4; i++)
          {
              if(positionsSelected[i + row] == 'x')
              {
                  fourInRowX++;
              }
              if(positionsSelected[i + row] == 'o')
              {
                  fourInRowO++;
              }
              
          }
          if (fourInRowX == 4)
          {
              //winner = 'x';
              return 'x';
          }
          if(fourInRowO == 4)
          {
              //winner = 'o';
              return 'o';
            
          }
          fourInRowX = 0;
          fourInRowO = 0;
      }
      return 'z';
  }
  
  char checkColumns()
  {
      int fourInColX = 0;
      int fourInColO = 0;
      
      for(int col = 0; col < 4; col++)
      {
          for(int i = 0; i < 16; i = i + 4)
          {
              if(positionsSelected[i + col] == 'x')
              {
                  fourInColX++;
              }
              if(positionsSelected[i + col] == 'o')
              {
                  fourInColO++;
              }
          }
          if(fourInColX == 4)
          {
              return 'x';
          }
          if(fourInColO == 4)
          {
              return 'o';
          }
          fourInColX = 0;
          fourInColO = 0;
      }
      return 'z';
  }
  char checkDiagonals()
  {
      int fourInDiagX = 0;
      int fourInDiagO = 0;
      for(int diag = 0; diag < 16; diag = diag + 5)
      {
          if(positionsSelected[diag] == 'x')
          {
              fourInDiagX++;
              
          }
          if(positionsSelected[diag] == 'o')
          {
              fourInDiagO++;
          }
          
      }
      if(fourInDiagX != 4 and fourInDiagO != 4)
      {
          fourInDiagX = 0;
          fourInDiagO = 0;
          for(int i = 3; i < 16; i = i + 3)
          {
              if(positionsSelected[i] == 'x')
              {
                  fourInDiagX++;
              }
              if(positionsSelected[i] == '0')
              {
                  fourInDiagO++;
              }
          }
          if(fourInDiagX == 4)
          {
              return 'x';
            
          }
          if(fourInDiagO == 4)
          {
              return 'o';
          }
          
      }
      return 'z';
  }
  
  char determineWinner()
  {
     winner = checkRows();
     if(winner == 'z')
     {
         winner = checkColumns();
     }
     if(winner == 'z')
     {
         winner = checkDiagonals();
     }
     return winner;
  }
  
};
void getUserNames(string &, string &);
void printBlankBoard();
void printTheBoard(Board, string);
void printUserPrompt(string, char);
void printGameWinner(Board, string, string);
int getUserResponse();
void checkResponse(Board&, char);
void writeTheBoard(Board);

using namespace std;
void getUserNames(string &userX, string &userO)
{
    cout << "Name of user to be 'x' : ";
    cin >> userX;
    cout << "Name of user to be 'o' : ";
    cin >> userO;
}

void checkResponse(Board &boardIn, char input)
{
    int position;
    int userInput;
    do
    {
        position = getUserResponse();
        userInput = boardIn.setPosition(position, input);
        if(userInput == -1)
        {
            cout << "That position already taken\n";      
            
        }
    }
    while(userInput == -1);
    
}
void printBlankBoard()
{
    for(int i = 0; i < 16; i++)
    {
        cout << "|" << i<<":";
        if(i <=9)
        {
            cout<<" ";
        }
        if(i%4 == 3)
        {
            cout << "|\n";
        }
    }
    cout << "\n\n";
}
void printTheBoard(Board boardIn)
{//print the board with player moves
    printBlankBoard();

    for(int i = 0; i <16; i++)
    {
        std::cout<<"|"<<boardIn.getPositions()[i];
        if(i%4 == 3)
        {
            std::cout<<"|\n";
        }
    }
    cout<<"\n\n\n";
}
/*void printTheBoard(Board boardIn)
{
    printBlankBoard();
    cout<<"\n";
    for(int i = 0; i < 16; i++)
    {
        cout << "|"<< boardIn.getPositions()[i];
        if(i%4 == 3)
        {
            cout<<"|\n";
        }
        
    }
    cout <<"\n\n";
}*/
void writeTheBoard(Board boardIn)
{
    cout<<"\n\n";
    for(int i = 0; i < 16; i++)
    {
        cout << "|"<< boardIn.getPositions()[i];
        
        if(i%4 == 3)
        {
            cout<<"|\n";
        }
        
    }
    cout <<"\n\n";
}
 void printUserPrompt(string nameIn, char letter)
 {
     cout<<nameIn<<" Where would you place an "<<letter<<" : \n\n";
 }
void printGameWinner(Board boardIn, string nameX, string nameO)
{
    char winner;
    winner = boardIn.determineWinner();
    if(winner == 'x')
    {
        cout<<"Congrats "<<nameX<< ", you won! \n\n";
    }
    if(winner == 'o')
    {
        cout<<"Congtrats "<<nameO << ", you won! \n\n";
    }
}

int getUserResponse()
{
    int position = -1;
    cout << " Enter an integer between 0 and 15 : \n";
    cin >> position;
    while(position > 15 || position < 0 || !cin )
    {
        cin.clear();
        cout <<" That is not a valied position \n";
        
        cout << "Enter an integer between 0 and 15 : \n";
        cin.clear();
        cin >> position;
    }
    return position;
    
    
}

//#include "mainClasses.cpp"
//#include "mainFunctions.cpp"

int main()
{
    Board gameBoard;
    string nameX, nameO;
    int tieGame = 0, numTurns = 0;
    char gameWinner = 'z';
    
    getUserNames(nameX, nameO);
    
    while(numTurns < 8)
    {
        printTheBoard(gameBoard);
        printUserPrompt(nameX, 'x');
        checkResponse(gameBoard, 'x');
        gameWinner = gameBoard.determineWinner();
        if(gameWinner !='z')
        {
            printTheBoard(gameBoard);
            writeTheBoard(gameBoard);
            printGameWinner(gameBoard, nameX, nameO);
            break;
        }
        
        printTheBoard(gameBoard);
        printUserPrompt(nameO, 'o');
        checkResponse(gameBoard, 'o');
        gameWinner = gameBoard.determineWinner();
        if(gameWinner !='z')
        {
            printTheBoard(gameBoard);
            writeTheBoard(gameBoard);
            printGameWinner(gameBoard, nameX, nameO);
            break;
        }
        numTurns++;
        
    }
    if(numTurns >=8)
    {
        cout<<"Tie game. \n\n";
    }
    return 0;
    
}