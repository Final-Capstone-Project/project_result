package biz.board.dao;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Component;

import biz.board.vo.BoardVO;

@Component("spring")
public class BoardDAO_spring implements BoardDAO{
	
	@Autowired
	JdbcTemplate template;
	
	@Override
	public List<BoardVO> getBoardList() {
		String sql = "select * from board order by board_id desc";
		return template.query(sql, new BoardRowMapper());
	}
	
	@Override
	public BoardVO getBoard(int board_id) {
		String sql = "select * from board where board_id = ?";
		return template.queryForObject(sql, new Object[] { board_id }, new BoardRowMapper());
	}

	@Override
	public int addBoard(BoardVO board) {
		String sql = "insert into board (board_id, title, content, writer) "
				+ "VALUES ((select max(board_id)+1 from board),?,?,?,?)";
		return template.update(sql, board.getTitle(), board.getContent(), board.getWriter());
	}

	@Override
	public int updateBoard(BoardVO board) {
		String sql = "update board set title = ?, content = ? where board_id = ?";
		return template.update(sql, new Object[] { board.getTitle(), board.getContent(), board.getWriter() });
	}

	@Override
	public int removeBoard(int board_id) {
		String sql = "delete from board where board_id = ?";
		return template.update(sql, new Object[] { board_id });
	}
	
	class BoardRowMapper implements RowMapper<BoardVO> {

		@Override
		public BoardVO mapRow(ResultSet rs, int rowNum) throws SQLException {
			BoardVO vo = new BoardVO();
			vo.setBoard_id(rs.getInt("board_id"));
			vo.setTitle(rs.getString("title"));
			vo.setContent(rs.getString("content"));
			vo.setWriter(rs.getString("writer"));
			
			return vo;
		}

	}
}
