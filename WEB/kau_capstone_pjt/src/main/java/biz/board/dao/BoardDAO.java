package biz.board.dao;

import java.util.List;
import biz.board.vo.BoardVO;

public interface BoardDAO {
	List<BoardVO> getBoardList();
	BoardVO getBoard(int board_id);
	int addBoard(BoardVO board);
	int updateBoard(BoardVO board);
	int removeBoard(int board_id);
}
