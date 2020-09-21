package biz.user.dao;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Component;

import biz.user.vo.UserVO;

@Component("spring")
public class UserDAO_spring implements UserDAO {

	@Autowired
	JdbcTemplate template;

	@Override
	public UserVO login(String id, String pw) {	      
		String sql = "select * from member where user_id=? and pw=?";
		UserVO vo = null;
		try {
			vo = template.queryForObject(sql, new Object[] { id, pw }, new UserRowMapper());
		} catch (Exception e) {

		}
		return vo;
	}
	
	@Override
	public UserVO getUser(String userid) {
		String sql = "select * from member where user_id = ?";
		UserVO vo = null;
		vo = template.queryForObject(sql, new Object[] {userid}, new UserRowMapper());
		return vo;
	}

	@Override
	public int addUser(UserVO user) throws Exception {
		String sql = "insert into member (user_id, pw, name) "
				+ "values (?, ?, ?)";

		return template.update(sql,user.getUser_id(), user.getPw(), user.getName());
	}

	@Override
	public int updateUser(UserVO user) {
		String sql = "update member set name=?, pw=? "
		 		+ " where  user_id  = ? ";
		return template.update(sql, new Object[] {user.getName(), user.getPw(), user.getUser_id()});
	}

	@Override
	public int removeUser(String userid) {
		String sql = "delete from member where  user_id  = ? ";
		return template.update(sql,new Object[] {userid});
	}

	class UserRowMapper implements RowMapper<UserVO>{
		@Override
		public UserVO mapRow(ResultSet rs, int rowNum) throws SQLException {
			UserVO vo = new UserVO();
			vo.setUser_id(rs.getString("user_id"));
			vo.setPw(rs.getString("pw"));
			vo.setName(rs.getString("name"));
			return vo;
		}
	}
	
}
