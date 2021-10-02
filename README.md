# LineTextProcessor
ラインの会話履歴（txt）をデータベース化するためのプログラム  
pythonをインタラクティブモードで起動する。その際に解析したいファイル名をコマンドライン引数として渡す。
あとはプログラムが自動で処理を行い、発言日時、発言者、発言内容をセットにしたディクショナリーをdataというリストに格納する。
（退会、参加、グループ名の変更などといったメンバーのアクションは省かれる）解析はそのdataに対して行われる。  
発言者の発言数と各日時の発言数をプロットする関数を用意してある。（ただし日本語は文字化けするので注意）  
showAllDaysGraphは発言が行われていない日も含めたグラフをプロットする。

A program to make a database of line(Japanese most famous SNS software) conversation history (txt).  
Run python in interactive mode. Pass the name of the file you want to analyze as a command line argument.
After that, the program will automatically process the file and store the dictionary with the date, time, speaker, and content in a list called "data".
(Member actions such as leaving, joining, changing the group name, etc. are omitted.)  
A function is provided to plot the number of chats by speaker and the number of chats for each date and time. (Note that Japanese characters will be garbled.)  
showAllDaysGraph plots a graph including days when no chats were made.
