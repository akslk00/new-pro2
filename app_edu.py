import pandas as pd
import streamlit as st


def run_edu_app():
    st.title('인천광역시 의료기관 현황')
    st.subheader('데이터')
    df=pd.read_csv('./data/incheon.csv',index_col=0, encoding='cp949')
    df=df.drop('Unnamed: 8',axis=1)
    df['병실수']=df['병실수'].fillna(0)
    df['진료과목']=df['진료과목'].fillna('보건진료소')
    st.dataframe(df)

    gang=df['군구명']=='강화군'
    ounm=df['군구명']=='옹진군'
    joun=df['군구명']=='중구'
    dong=df['군구명']=='동구'
    mechu=df['군구명']=='미추홀구'
    unesu=df['군구명']=='연수구'
    namdong=df['군구명']=='남동구'
    bupang=df['군구명']=='부평구'
    gaeyuan=df['군구명']=='계양구'
    sugu=df['군구명']=='서구'
    
    GA=df.loc[gang,]
    ga=['강화읍','내가면','송해면','길상면']
    UJ=df.loc[ounm,]
    uj=['백령면','연평면','연흥면']
    JG=df.loc[joun,]
    jg=['중산동','항동','용동','경동','운서동','율목동','운남동','인현동','신포동','신흥동','유동','답동'
        ,'내동','신생동','송월동']
    DG=df.loc[dong,]
    dg=['만석동','송림동','화수동','송현동','금곡동','화평동']
    MC=df.loc[mechu,]
    mc=['주안동','숭의동','용현동','학익동','도화동','문학동','관교동']
    US=df.loc[unesu,]
    us=['동춘동','연수동','청학동','옥련동','송도동','선학동']
    ND=df.loc[namdong,]
    nd=['구월동','논현동','간석동','서창동','만수동','도림동','고잔동','남촌동']
    BP=df.loc[bupang,]
    bp=['구산동','부평동','산곡동','삼산동','청천동','십정동','부개동',
        '갈산동','일신동']
    GY=df.loc[gaeyuan,]
    gy=['계산동','작전동','효성동','갈현동','임학동','용종동','병방동','박촌동','귤현동','동양동']
    SG=df.loc[sugu,]
    sg=['석남동','심곡동','왕길동','가좌동','원당동','청라동','연희동'
        ,'마전동','경서동','대곡동','가정동','당하동','신현동','검암동'
        ,'불로동','오류동']
    
    list_1 = ['내과','안과','치과','외과','소아과']

    #ef inchon():
        



    st.text('군구명을 선택하시오.')
    if st.checkbox('강화군'):
        ga_choice=st.selectbox('동을 선택해주새요.',ga)
        if ga_choice == ga[0]:
            list_1_cho = st.selectbox('과목을 선택하시오',list_1)
            if list_1_cho == list_1[0]:
                st.dataframe((GA.loc[(GA['소재지'].str.contains(ga[0])&GA['진료과목'].str.contains(list_1[0])),]))
            elif list_1_cho ==list_1[1]:
                st.dataframe((GA.loc[(GA['소재지'].str.contains(ga[0])&GA['진료과목'].str.contains(list_1[1])),]))
        elif ga_choice == ga[1]:
            list_1_cho = st.selectbox('과목을 선택하시오',list_1)
            if list_1_cho == list_1[0]:
                if True:
                    st.dataframe((GA.loc[(GA['소재지'].str.contains(ga[1])&GA['진료과목'].str.contains(list_1[0])),]))
                elif False:
                    st.text('일치하는 데이터가 없습니다.')
            elif list_1_cho ==list_1[1]:
                if True:
                    st.dataframe((GA.loc[(GA['소재지'].str.contains(ga[1])&GA['진료과목'].str.contains(list_1[1])),]))
                elif False:
                    st.text('일치하는 데이터가 없습니다.')
        elif ga_choice == ga[2]:
            st.dataframe(GA.loc[GA['소재지'].str.contains('송해면'),])
        elif ga_choice == ga[3]:
            st.dataframe(GA.loc[GA['소재지'].str.contains('길상면'),])

    if st.checkbox('옹진군'):
        uj_choice=st.selectbox('동을 선택해주새요.',uj)
        if uj_choice == uj[0]:
            st.dataframe(UJ.loc[UJ['소재지'].str.contains('백령면'),])
        elif uj_choice == uj[1]:
            st.dataframe(UJ.loc[UJ['소재지'].str.contains('연평면'),])
        elif uj_choice == uj[2]:
            st.dataframe(UJ.loc[UJ['소재지'].str.contains('연흥면'),])

    if st.checkbox('중구'):
        jg_choice=st.selectbox('동을 선택해주새요.',jg)
        if jg_choice == jg[0]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('중산동'),])
        elif jg_choice == jg[1]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('항동'),])
        elif jg_choice == jg[2]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('용동'),])
        elif jg_choice == jg[3]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('경동'),])
        elif jg_choice == jg[4]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('운서동'),])
        elif jg_choice == jg[5]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('운남동'),])
        elif jg_choice == jg[6]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('인현동'),])
        elif jg_choice == jg[7]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('신포동'),])
        elif jg_choice == jg[8]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('신흥동'),])
        elif jg_choice == jg[9]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('유동'),])
        elif jg_choice == jg[10]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('답동'),])
        elif jg_choice == jg[11]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('내동'),])
        elif jg_choice == jg[12]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('신생동'),])
        elif jg_choice == jg[13]:
            st.dataframe(JG.loc[JG['소재지'].str.contains('송월동'),])

    if st.checkbox('동구'):
        dg_choice=st.selectbox('동을 선택해주새요.',dg)
        if dg_choice == dg[0]:
            st.dataframe(DG.loc[DG['소재지'].str.contains('만석동'),])
        elif dg_choice == dg[1]:
            st.dataframe(DG.loc[DG['소재지'].str.contains('송림동'),])
        elif dg_choice == dg[2]:
            st.dataframe(DG.loc[DG['소재지'].str.contains('화수동'),])
        elif dg_choice == dg[3]:
            st.dataframe(DG.loc[DG['소재지'].str.contains('송현동'),])
        elif dg_choice == dg[4]:
            st.dataframe(DG.loc[DG['소재지'].str.contains('금곡동'),])
        elif dg_choice == dg[5]:
            st.dataframe(DG.loc[DG['소재지'].str.contains('화평동'),])

    if st.checkbox('미추홀구'):
        mc_choice=st.selectbox('동을 선택해주새요.',mc)
        if mc_choice == mc[0]:
            st.dataframe(MC.loc[MC['소재지'].str.contains('주안동'),])
        elif mc_choice == mc[1]:
            st.dataframe(MC.loc[MC['소재지'].str.contains('숭의동'),])
        elif mc_choice == mc[2]:
            st.dataframe(MC.loc[MC['소재지'].str.contains('용현동'),])
        elif mc_choice == mc[3]:
            st.dataframe(MC.loc[MC['소재지'].str.contains('학익동'),])
        elif mc_choice == mc[4]:
            st.dataframe(MC.loc[MC['소재지'].str.contains('도화동'),])
        elif mc_choice == mc[5]:
            st.dataframe(MC.loc[MC['소재지'].str.contains('문학동'),])
        elif mc_choice == mc[6]:
            st.dataframe(MC.loc[MC['소재지'].str.contains('관교동'),])

    if st.checkbox('연수구'):
        us_choice=st.selectbox('동을 선택해주새요.',us)
        if us_choice == us[0]:
            st.dataframe(US.loc[US['소재지'].str.contains('동춘동'),])
        elif us_choice == us[1]:
            st.dataframe(US.loc[US['소재지'].str.contains('연수동'),])
        elif us_choice == us[2]:
            st.dataframe(US.loc[US['소재지'].str.contains('청학동'),])
        elif us_choice == us[3]:
            st.dataframe(US.loc[US['소재지'].str.contains('옥련동'),])
        elif us_choice == us[4]:
            st.dataframe(US.loc[US['소재지'].str.contains('송도동'),])
        elif us_choice == us[5]:
            st.dataframe(US.loc[US['소재지'].str.contains('선학동'),])

    if st.checkbox('남동구'):
        nd_choice=st.selectbox('동을 선택해주새요.',nd)
        if nd_choice == nd[0]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('구월동'),])
        elif nd_choice == nd[1]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('논현동'),])
        elif nd_choice == nd[2]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('간석동'),])
        elif nd_choice == nd[3]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('서창동'),])
        elif nd_choice == nd[4]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('만수동'),])
        elif nd_choice == nd[5]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('도림동'),])
        elif nd_choice == nd[6]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('고잔동'),])
        elif nd_choice == nd[7]:
            st.dataframe(ND.loc[ND['소재지'].str.contains('남촌동'),])
            
    if st.checkbox('부평구'):
        bp_choice=st.selectbox('동을 선택해주새요.',bp)
        if bp_choice == bp[0]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('구산동'),])
        elif bp_choice == bp[1]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('부평동'),])
        elif bp_choice == bp[2]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('산곡동'),])
        elif bp_choice == bp[3]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('삼산동'),])
        elif bp_choice == bp[4]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('청천동'),])
        elif bp_choice == bp[5]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('십정동'),])
        elif bp_choice == bp[6]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('부개동'),])
        elif bp_choice == bp[7]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('갈산동'),])
        elif bp_choice == bp[8]:
            st.dataframe(BP.loc[BP['소재지'].str.contains('일신동'),])

    if st.checkbox('계양구'):
        gy_choice=st.selectbox('동을 선택해주새요.',gy)
        if gy_choice == gy[0]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('계산동'),])
        elif gy_choice == gy[1]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('작전동'),])
        elif gy_choice == gy[2]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('효성동'),])
        elif gy_choice == gy[3]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('갈현동'),])
        elif gy_choice == gy[4]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('임학동'),])
        elif gy_choice == gy[5]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('용종동'),])
        elif gy_choice == gy[6]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('병방동'),])
        elif gy_choice == gy[7]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('박촌동'),])
        elif gy_choice == gy[8]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('귤현동'),])
        elif gy_choice == gy[9]:
            st.dataframe(GY.loc[GY['소재지'].str.contains('동양동'),])

    if st.checkbox('서구'):
        sg_choice=st.selectbox('동을 선택해주새요.',sg)
        if sg_choice == sg[0]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('석남동'),])
        elif sg_choice == sg[1]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('심곡동'),])
        elif sg_choice == sg[2]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('왕길동'),])
        elif sg_choice == sg[3]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('가좌동'),])
        elif sg_choice == sg[4]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('원당동'),])
        elif sg_choice == sg[5]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('청라동'),])
        elif sg_choice == sg[6]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('연희동'),])
        elif sg_choice == sg[7]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('마전동'),])
        elif sg_choice == sg[8]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('경서동'),])
        elif sg_choice == sg[9]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('계산동'),])
        elif sg_choice == sg[10]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('대곡동'),])
        elif sg_choice == sg[11]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('가정동'),])
        elif sg_choice == sg[12]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('당하동'),])
        elif sg_choice == sg[13]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('신현동'),])
        elif sg_choice == sg[14]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('검암동'),])
        elif sg_choice == sg[15]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('불로동'),])
        elif sg_choice == sg[16]:
            st.dataframe(SG.loc[SG['소재지'].str.contains('오류동'),])
