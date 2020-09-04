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
	      String sql = "";
	      UserVO vo = null;

	      return vo;
	   }

	@Override
	public int addUser(UserVO user) throws Exception {
		
		return 0;
	}

	@Override
	public int updateUser(UserVO user) {
		 
		return 0;
	}

	@Override
	public int removeUser(String userid) {
		
		return 0;
	}

	class UserRowMapper implements RowMapper<UserVO>{
		@Override
		public UserVO mapRow(ResultSet rs, int rowNum) throws SQLException {
			UserVO vo = new UserVO();
			
			// vo.set???(rs.get??(" "))
			
			return vo;
		}
	}
	
}