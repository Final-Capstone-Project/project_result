package biz.user.dao;

import java.util.List;

import biz.user.vo.UserVO;

public interface UserDAO {
	
	UserVO login(String id, String pw);
	UserVO getUser(String id);
	int addUser(UserVO user) throws Exception;
	int updateUser(UserVO user);
	int removeUser(String userid);
}
