package biz.board.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import biz.board.dao.BoardDAO;
import biz.board.vo.BoardVO;

@Service("boardservice")
public class BoardServiceImpl implements BoardService {

	@Autowired
	@Qualifier("spring")
	BoardDAO dao;
	
	public BoardServiceImpl() {
		super();
	}
	
	public BoardServiceImpl(BoardDAO dao) {
		super();
		this.dao = dao;
	}
	
	@Override 
	public List<BoardVO> getBoardList() {
		return dao.getBoardList();
	}
	
	@Override
	public BoardVO getBoard(int board_id) {
		return dao.getBoard(board_id);
	}

	@Override
	public int addBoard(BoardVO board) {
		return dao.addBoard(board);
	}

	@Override
	public int updateBoard(BoardVO board) {
		return dao.updateBoard(board);
	}

	@Override
	public int removeBoard(int board_id) {
		return dao.removeBoard(board_id);
	}
	
}
