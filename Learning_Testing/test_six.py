from six import Person
import pytest, time


class Testsix:
    
    @pytest.fixture
    def setup(self):
        self.p1 = Person('Ali', 'Pourzad')
        self.p2 = Person('Hossein', 'Tahami')
        yield 'setup'
        time.sleep(0.3)
        
    def test_fullname(self, setup):
        assert self.p2.fullname() == 'Hossein Tahami'
        assert self.p1.fullname() == 'Ali Pourzad'
    
    def test_email(self, setup):        
        assert self.p2.email() == 'HosseinTahami@email.com'
        assert self.p1.email() == 'AliPourzad@email.com'
        
    
