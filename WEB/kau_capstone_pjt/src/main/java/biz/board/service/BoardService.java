package biz.board.service;

import biz.board.vo.BoardVO;

public interface BoardService {
	List<BoardVO> getBoardList();
	BoardVO getBoard(int board_id);
	int addBoard(BoardVO board);
	int updateBoard(BoardVO board);
	int removeBoard(int board_id);
}
