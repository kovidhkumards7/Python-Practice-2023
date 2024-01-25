class Dis():
    dis = 0
    @staticmethod
    def cal_dis(ar):
        if ar == "member":
            Dis.dis = 0.3
        else:
            Dis.dis = 0.1
        return Dis.dis

print(Dis.cal_dis("member"))