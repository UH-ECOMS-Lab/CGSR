def train_candidate(model, input_data, hr_img, hr_cg, feature_reg, shrink_channels, num_epochs=5, lr=1e-4):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    model.train()    
    for epoch in range(num_epochs):
        optimizer.zero_grad()        
        sr_img, sr_cg_info = model(input_data)
        loss = compute_loss(hr_img, sr_img, hr_cg, sr_cg_info, feature_reg, shrink_channels)
        loss.backward()
        optimizer.step()    
    return model

model_CGO = CGE_arch.CGE(in_nc=3, out_nc=3, nf=40, unf=24, nb=16, scale=scale)
model_weight = torch.load('CG-enhanced/model.pth')
model_CGO.load_state_dict(model_weight, strict=False)
num_gen = num_gen
num_cand = num_cand
para_list = []
cand_list = []

for i in range (num_cand):
    cand_list.append([[],[],[],[],[]])
for i in range (num_gen):
    print("Generation:")
    print(i)
    for j in range(num_cand):
        if j < num_cand/2:
            pop = num_cand
            parent = random.randint(0, pop)
            new_cand = copy.deepcopy(cand_list[-parent])
            new_cand = mutation(new_cand)
            model = copy.deepcopy(model_CGO)
            model = list_to_model(model, new_cand)
            #Warm start training
            model = train_candidate(model, input_data, hr_img, hr_cg, feature_reg, shrink_channels)
            #Evaluation
            psnr, para = test(model)
            cand_list.append(new_cand)
            para_list.append(para)
        else:
            pop = num_cand
            parent1 = random.randint(0, pop)
            parent2 = random.randint(0, pop)
            new1 = copy.deepcopy(cand_list[-parent1])
            new2 = copy.deepcopy(cand_list[-parent2])
            new_cand = crossover(new1, new2)
            model = copy.deepcopy(model_CGO)
            model = list_to_model(model, new_cand)
            #Warm start training
            model = train_candidate(model, input_data, hr_img, hr_cg, feature_reg, shrink_channels)
            #Evaluation
            psnr, para = test(model)
            cand_list.append(new_cand)
            para_list.append(para)

index_min = np.argmin(para_list)
best = cand_list[index_min]    
model = copy.deepcopy(model_CGO)
model = list_to_model(model, new_cand)
print("Final: Para")
print(para_list[index_min])
PATH = "CG-optimized/model.pth"
torch.save(model.state_dict(), PATH)
