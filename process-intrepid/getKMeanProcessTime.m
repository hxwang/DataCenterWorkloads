 

%load data, and convert seconds to hours
meas = load('..\data\ANL-Intrepid-2009-1.swf\processTime.txt')./3600;

%kmean cluster with 10 centers
%[idx, c] = kmeans(data, 10);

[clusters,c] = kmeans(meas, 6);

cluster1 = meas(clusters == 1, :);
cluster2 = meas(clusters == 2, :);
cluster3 = meas(clusters == 3, :);
cluster4 = meas(clusters == 4, :);
cluster5 = meas(clusters == 5, :);
cluster6 = meas(clusters == 6, :);
% cluster7 = meas(clusters == 7, :);
% cluster8 = meas(clusters == 8, :);
% cluster9 = meas(clusters == 9, :);
% cluster10 = meas(clusters == 10, :);

figure1 = figure;
set(figure1,'units','normalized','outerposition',[0 0 1 1]);

axes1 = axes('Parent',figure1);
box(axes1,'on');
hold(axes1,'all');
set(axes1,'FontSize',30,'FontWeight','bold');


plot(cluster1(:, [1]), '*', 'color', 'b'); hold all
plot(cluster2(:, [1]), '*', 'color', 'r')
plot(cluster3(:, [1]), '*', 'color', 'c')
plot(cluster4(:, [1]), '*', 'color', 'm')
plot(cluster5(:, [1]), '*', 'color', 'g')
plot(cluster6(:, [1]), '*', 'color', 'y')
% plot(cluster7(:, [1]), '*', 'color', 'k')
% plot(cluster8(:, [1]), '*', 'color', [0.5 0.5 0])
% plot(cluster9(:, [1]), '*', 'color', [1 0.5 0])
% plot(cluster10(:, [1]), '*', 'color', [0.5 0 1])

ylabel('processing time (hour)')
xlabel('count')

%save figure
set(gcf, 'PaperPosition', [0 0 13 7]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [13 7]); %Set the paper to have width 5 and height 5.

%path

saveas(gca, strcat(pwd,'\figs\processingTimeHist_k-mean', '.eps'),'psc2') %Save figure 
saveas(gcf, strcat(pwd ,'\figs\processingTimeHist_k-mean'), 'pdf') %Save figure 
saveas(gcf, strcat(pwd ,'\figs\processingTimeHist_k-mean'), 'png') %Save figure 