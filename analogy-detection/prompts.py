annual_report_messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"I want you to look at the following excerpt from an {industry} industry annual report and decide whether "
                "the author(s) make any analogical references to other industries. "
                "Identify and highlight explicit analogical references in the annual report where the company directly compares its operations or situation to those in specific other industries. "
                "Some examples of this would be 'This is similar to [specific industry],' or 'Our situation resembles that of [specific industry].'"
                ""
                "Your respone should be either 'No' or 'Yes: [Quote from excerpt containing analogical reference] [reasoning/explanation]'. "
                ""
                "That is, if the text contains an anological reference of this sort, report it "
                "specifically as a quote from the text. If there is no useful information in the text, output 'No.'"}, 
        {"role": "system", "content": "Sure, I can help you with that. Please provide me with the text you would like me to analyze."},
        {"role": "user", "content": stext}
        ]

news_articles_messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"I want you to look at the following excerpt from a news article about power marketing and decide whether "
                "the author(s) make any analogical references to other industries. "
                "Identify and highlight explicit analogical references in the article where the article directly compares power marketing operations or situations to those in specific other industries. "
                "Some examples of this would be 'This is similar to [specific industry],' or 'Our situation resembles that of [specific industry].'"
                ""
                "Your respone should be either 'No' or 'Yes: [Quote from excerpt containing analogical reference] [reasoning/explanation]'. "
                ""
                "That is, if the text contains an anological reference of this sort, report it "
                "specifically as a quote from the text. If there is no useful information in the text, output 'No.'"}, 
        {"role": "system", "content": "Sure, I can help you with that. Please provide me with the text you would like me to analyze."},
        {"role": "user", "content": stext}
        ]

cap_iq_messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"I want you to look at the following excerpt from an earnings call and decide whether "
                "the author(s) make any analogical references to other industries. "
                "Identify and highlight explicit analogical references in the annual report where the company directly compares its operations or situation to those in specific other industries. "
                "Some examples of this would be 'This is similar to [specific industry],' or 'Our situation resembles that of [specific industry].'"
                ""
                "Your respone should be either 'No' or 'Yes: [Quote from excerpt containing analogical reference] [reasoning/explanation]'. "
                ""
                "That is, if the text contains an anological reference of this sort, report it "
                "specifically as a quote from the text. If there is no useful information in the text, output 'No.' Make sure your reasoining takes into account the industry of the company giving the presentation."}, 
        {"role": "system", "content": "Sure, I can help you with that. Please provide me with the text you would like me to analyze."},
        {"role": "user", "content": stext}
        ]