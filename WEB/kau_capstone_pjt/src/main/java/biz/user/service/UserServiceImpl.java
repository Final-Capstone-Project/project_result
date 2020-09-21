package biz.user.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import biz.user.dao.UserDAO;
import biz.user.vo.UserVO;

@Service("userservice")
public class UserServiceImpl implements UserService{
	
	@Autowired
	@Qualifier("spring")
	UserDAO dao;
	
	public UserServiceImpl() {
		super();
	}
	public UserServiceImpl(UserDAO dao) {
		super();
		this.dao = dao;
	}

	@Override
	public UserVO login(String id, String pw) {
		return dao.login(id, pw);
	}
	
	@Override
	public UserVO getUser(String id) {
		return dao.getUser(id);
	}

	@Override
	public int addUser(UserVO user) throws Exception {
		return dao.addUser(user);
	}

	@Override
	public int updateUser(UserVO user) {
		return dao.updateUser(user);
	}

	@Override
	public int removeUser(String userid) {
		return dao.removeUser(userid);
	}
	
}
