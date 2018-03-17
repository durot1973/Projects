# Importing the dataset
college = read.csv('College.csv')

# Setting the row names and removing the column of names
rownames(college) = college[, 1]

college = college[, -1]

# Getting a summary of the dataset
summary(college)

# EDA
college$Private = as.factor(college$Private)

# Doing some boxplots
plot(x=college$Private, y=college$Outstate, xlab='Private', ylab='Out of State Tuition',
     main='Private School tuition?')

# Getting Elite Schools and adding to the dataframe
Elite = rep('No', nrow(college))
Elite[college$Top10perc > 50] = 'Yes'
Elite = as.factor(Elite)
college = data.frame(college, Elite)

# Comparing the cost of Elite schools with out of State tuition
plot(x=college$Elite, y=college$Outstate, xlab='Elite', ylab='Out of State Tuition',
     main='Elite School tuition?')

# Plotting Some histograms
hist(college$PhD, main = 'Histogram of  the number of PhD Faculty Members',
     xlab = 'PhD Faculty Members')

# Comparing cost of living of elite schools vs non-elite schols
plot(x=college$Elite, y=college$Personal,
     xlab='Elite', ylab='Cost of Living',
     main='Cost of living for Elite vs Non-Elite Schools')