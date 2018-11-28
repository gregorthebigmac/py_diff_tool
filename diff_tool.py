import os

def get_dir(m_root_dir, m_sub_dirs, m_filenames):
	for m_root_dir, m_sub_dirs, m_filenames in os.walk(m_root_dir):
		m_sub_dirs.sort()
		for m_sub_sub_dirs in m_sub_dirs:
			m_sub_sub_dirs.sort()
			m_filenames.sort()
	return m_sub_dirs, m_filenames

root_dir = raw_input("what path?")
root_dir, sub_dirs, filenames = get_dir(root_dir, sub_dirs, filenames)
