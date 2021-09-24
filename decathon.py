import re
import requests
import pandas as pd

col_names =  ['name', '100m','long_jump','shot_put', 'high_jump', '400m', '110m_hurdles', 'discus_throw','pole_vault', 'javelin_throw', '1500m']

class ComputeDecathon:
    def __init__(self, url:str = None) -> None:
        self.__doc_url = url
        self.__headers = {
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54',
                            'accept': 't	text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'cross-site',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'referer': 'https://www.google.com/',
                            'accept-language': 'en-US,en;q=0.9',
                            }
        if self.__doc_url is not None:
            self.__validate_input(self.__doc_url)
            self.__data = self.__validate_doc_exist(self.__doc_url, self.__headers)

    @staticmethod
    def __validate_input(url: str) -> None:

        """
            Check if the url passed is a valid string

            Parameters
            ----------
                url: string
                    The url of the webpage

            returns
            --------
                bool

        """

        if not isinstance(url, str):
            raise TypeError('accepted type is string for url')

    def __validate_doc_exist(self, url: str, headers) -> tuple:
        """
            Checks if the supplied url is valid and returns a response
        """
        try:
            return pd.read_csv(url,sep=';', header=None, names=col_names )
        except Exception as error:
            raise ValueError (f"Error with supplied url: {error}")

        
    def score_100m(self, secs_round):
        return round(25.4347 * pow((18 - secs_round), 1.81),0)

    def score_long_jum(self, meters_jumped):
        return round(0.14354 * pow(((meters_jumped * 100) - 220), 1.4),0)

    def score_shot_put(self, metres_thrown):
        return round(51.39 * pow((metres_thrown  - 1.5), 1.05),0)
        
    def score_high_jump(self, metres_jumped):
        return 1000 if metres_jumped >= 2.20 else  int(round(0.8465 * pow(((metres_jumped * 100) - 75), 1.42), -2))

    def score_400m(self, sec_ran):
        return round(1.53775 * pow((82 - sec_ran), 1.81),0)

    def score_110_hurdles(self, sec_ran):
        return 1000 if round(5.74352 * pow((28.5 - sec_ran), 1.92),0) > 1000 else round(5.74352 * pow((28.5 - sec_ran), 1.92),0)

    def score_discus_throw(self, metres):
        return round(12.91 * pow((metres  - 4), 1.1),0)

    def score_pole_vault(self,metres_jumped):
        return 1000 if metres_jumped >= 5.28 else  int(round(0.2797 * pow(((metres_jumped * 100) - 100), 1.35), -2))

    def score_javelin(self, metres):
        return round(10.14 * pow((metres  - 7), 1.08),0)

    def score_1500m(self, mins_sec):
        split_time = re.split('[.|:]', mins_sec)
        #split_time = mins_sec.split('.')
        secs = (60 * int(split_time[0])) + int(split_time[1]) + (int(split_time[-1])/1000)
        return 1000 if  round(0.03768 * pow((480 - secs), 1.85),0) > 1000 else round(0.03768 * pow((480 - secs), 1.85),0) 
    
    def get_score_and_rank(self) -> pd.DataFrame:
        if self.__doc_url is not None:
            self.__data = self.__compute_score()
            self.__data = self.__arrange_score()
   
            return self.__data[['name', '100m', 'long_jump', 'shot_put', 'high_jump', '400m',
                                '110m_hurdles', 'discus_throw', 'pole_vault', 'javelin_throw', '1500m', 'score','placement']]
        else:
            return None

    def __compute_score(self):
        if self.__doc_url is not None:
            m100 = self.__data['100m'].apply(lambda x: self.score_100m(x))
            long_jump = self.__data['long_jump'].apply(lambda x: self.score_long_jum(x))
            shot_pu = self.__data['shot_put'].apply(lambda x: self.score_shot_put(x))
            high_jump = self.__data['high_jump'].apply(lambda x: self.score_high_jump(x))
            m400 = self.__data['400m'].apply(lambda x: self.score_400m(x))
            hurdles = self.__data['110m_hurdles'].apply(lambda x: self.score_110_hurdles(x))
            discus = self.__data['discus_throw'].apply(lambda x: self.score_discus_throw(x))
            pole = self.__data['pole_vault'].apply(lambda x: self.score_pole_vault(x))
            m1500 =  self.__data['1500m'].apply(lambda x: self.score_1500m(x))

            self.__data['score'] = m100 + long_jump + shot_pu + high_jump + m400 + hurdles + discus + pole + m1500
            return self.__data
        else:
            return None

    def __get_ranking(self, min_rank, max_rank):
        if min_rank == max_rank:
            return min_rank
        else:
            return f'{min_rank} - {max_rank}'

    def __arrange_score(self):
        
        self.__data["Rank_max"] = self.__data["score"].rank(ascending = False, method = 'max').astype(int)
        self.__data["Rank_min"] = self.__data["score"].rank(ascending = False, method = 'min').astype(int)
        self.__data["placement"] = self.__data.apply(lambda dat: self.__get_ranking(dat['Rank_min'], dat['Rank_max']), axis = 1)
        return self.__data


